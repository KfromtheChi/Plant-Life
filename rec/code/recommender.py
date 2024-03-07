import pandas as pd
import numpy as np

import ast

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import make_column_selector, ColumnTransformer
from sklearn.impute import SimpleImputer

# Helper function for later
def __score_bucketer(n):
    if n > 0.9:
        return 'High'
    elif n > 0.75:
        return 'Moderate'
    return 'Low'

# These lines read in plant data
__plants = pd.read_csv('../data/plants.csv')
__reduced = pd.read_csv('../data/reduced.csv')

# Removes the id column to prep for later
__reduced.drop(columns = ['id'], inplace = True)


# Reformats some columns to be usable
__plants['scientific_name'] = __plants['scientific_name'].apply(ast.literal_eval)
__plants['origin'] = __plants['origin'].apply(ast.literal_eval)
__plants['dimensions'] = __plants['dimensions'].apply(ast.literal_eval)
__plants['attracts'] = __plants['attracts'].apply(ast.literal_eval)
__plants['propagation'] = __plants['propagation'].apply(ast.literal_eval)
__plants['hardiness'] = __plants['hardiness'].apply(ast.literal_eval)
__plants['depth_water_requirement'] = __plants['depth_water_requirement'].apply(ast.literal_eval)
__plants['volume_water_requirement'] = __plants['volume_water_requirement'].apply(ast.literal_eval)
__plants['plant_anatomy'] = __plants['plant_anatomy'].apply(ast.literal_eval)
__plants['sunlight'] = __plants['sunlight'].apply(ast.literal_eval)
__plants['pruning_count'] = __plants['pruning_count'].apply(ast.literal_eval)
__plants['soil'] = __plants['soil'].apply(ast.literal_eval)
__plants['pest_susceptibility'] = __plants['pest_susceptibility'].apply(ast.literal_eval)
__plants['leaf_color'] = __plants['leaf_color'].apply(ast.literal_eval)

# Creates hardiness bounds
__plants['hardiness_min'] = __plants['hardiness'].apply(lambda x: int(x['min']) if len(x['min']) else 1)
__plants['hardiness_max'] = __plants['hardiness'].apply(lambda x: int(x['max']) if len(x['max']) else 12)


# Recodes sunlight
__plants['sunlight'] = __plants['sunlight'].apply(lambda x: [i.strip().lower().title() for i in x])
to_full = ['Full Sun', 'Sun', 'Full Sun Only If Soil Kept Moist']
part_shade = [
    'Part Shade', 'Filtered Shade', 'Part Sun/Part Shade', 'Partial Shade', 'Partial Sun Shade', 'Sun-Part Shade',
    'Deciduous Shade (Spring Sun)', 'Full Sun Partial Sun Shade'
]
part_sun = [
    'Full Sun Partial Sun', 'Partial Sun'
]

def __sun_fixer(string):
    if string in to_full:
        return 'Full Sun'
    elif string in part_shade:
        return 'Partial Shade'
    elif string in part_sun:
        return 'Partial Sun'
    else:
        return 'Full Shade'

__plants['sunlight_simplified'] = __plants['sunlight'].apply(lambda x: __sun_fixer(x[-1]) if len(x) else 'N/A')


# Recodes care
med = ['Medium', 'Moderate', 'Regular']
low = ['Low', 'Easy']
hi  = ['High', 'Extreme']


def __care_fixer(string):
    if string in med:
        return 'Moderate'
    elif string in low:
        return 'Low'
    elif string in hi:
        return 'High'

__plants['care_level'] = __plants['care_level'].apply(__care_fixer)

# Fills in missing dimension data
__reduced['dimension_max'] = SimpleImputer().fit_transform(__reduced[['dimension_max']])
__reduced['dimension_min'] = SimpleImputer().fit_transform(__reduced[['dimension_min']])

# Objects for prepping data for use
__ct = ColumnTransformer(
    [
        ('ohe', OneHotEncoder(sparse_output = False, min_frequency = 20), make_column_selector(dtype_exclude = np.number))
    ],
    remainder = 'passthrough'
)

__pipeline = Pipeline(
    [
        ('ct', __ct),
        ('mm', MinMaxScaler())
    ]
)

# Transformed data, ready to create recommendations
X = __pipeline.fit_transform(__reduced)


# Defines function to take in a set of ids and return the row

def generate_recommendations(ids: list): 
    # Gather and transform selected plants
    seeds = pd.DataFrame(__pipeline.transform(__reduced.loc[np.array(ids) - 1, :]))
    # Calculate similarity matrix of selected vs remaining plants
    sims = pd.DataFrame(cosine_similarity(seeds, __pipeline.transform(__reduced.drop(seeds.index))))

    # Take top 10 most similar plants for each selected plant
    top_10_scores = []

    for i in range(sims.shape[0]):
        scores = sims.iloc[i, :].sort_values(ascending = False).iloc[0:10]
        top_10_scores.append(pd.DataFrame(zip(scores.index, scores.values), columns = ['id', 'score']))
    
    all_scores = pd.concat(top_10_scores).reset_index(drop = True)

    # Take average score across each plant in set of top 10 scores
    top_10 = all_scores.groupby('id').mean().sort_values(by = 'score', ascending = False)[:10]

    # Select most similar plants
    best_scores = __plants.loc[top_10['score'].index, ['id', 'common_name', 'scientific_name', 'description']]
    # Assign a rating based on score
    best_scores['rating'] = top_10['score'].apply(__score_bucketer)
    best_scores['scientific_name'] = best_scores['scientific_name'].apply(lambda x: x[0])

    # Returns a list of dicts where each dict is the info for one plant
    output = []

    for _, row in best_scores.iterrows():
        output.append(row.to_dict())

    return output


# Creates list based on filters from quiz
def populate_list(filters):
    hardiness_check = (__plants['hardiness_min'] <= filters['hardiness_zone']) & (filters['hardiness_zone'] <= __plants['hardiness_max'])
    sun_check = __plants['sunlight_simplified'].isin(filters['sun_options'])
    water_check = __plants['watering'].isin(filters['water_options'])
    care_check = __plants['care_level'].isin(filters['care_levels'])

    indices = __plants[hardiness_check & sun_check & water_check & care_check].sample(20)[['id', 'common_name', 'scientific_name', 'description']]
    indices['scientific_name'] = indices['scientific_name'].apply(lambda x: x[0])
    output = []

    for _, row in indices.iterrows():
        output.append(row.to_dict())

    return output