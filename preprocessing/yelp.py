# NOTE: Delete the following data sets from Yelp Dataset folder:
# - yelp_academic_dataset_checkin.json
# - yelp_academic_dataset_tip.json


import pandas as pd

# Change chunk size according to what your computer can handle,
# but smaller chunk size means longer processing times.
CHUNK_SIZE = 20000
DATASETS_FOLDER_PATH = '../datasets'

dataset_paths = {
    'user': f'{DATASETS_FOLDER_PATH}/yelp_academic_dataset_user.json',
    'review': f'{DATASETS_FOLDER_PATH}/yelp_academic_dataset_review.json',
    'business': f'{DATASETS_FOLDER_PATH}/yelp_academic_dataset_business.json'
}

columns_to_drop = {
    'user': ['yelping_since', 'elite', 'friends',
             'compliment_list', 'compliment_more', 'compliment_note',
             'compliment_photos', 'compliment_profile',
             'compliment_cool', 'cool', 'fans', 'compliment_cute', 'funny',
             'compliment_funny', 'review_count', 'compliment_hot', 'compliment_writer',
             'name', 'useful', 'compliment_plain'],
    'review': ['cool', 'date', 'funny', 'review_id', 'text', 'useful'],
    'business': ['is_open', 'name', 'review_count',
                 'address', 'city', 'state', 'attributes', 'hours', 'neighborhood']
}


def get_z_score_for_type(df, dataset_type):
    if dataset_type == 'user':
        return (df['average_stars'] - df['average_stars'].mean()) / (df['average_stars'].std())
    else:
        return (df['stars'] - df['stars'].mean()) / (df['stars'].std())


for dataset_type in ['user', 'review', 'business']:
    infile_path = dataset_paths[dataset_type]
    outfile_path = f'{DATASETS_FOLDER_PATH}/yelp_{dataset_type}_processed.json'

    with open(infile_path, encoding='utf-8') as readfile, open(outfile_path, 'w') as writefile:
        # Read file chunks at a time in order to handle large files
        print(f'Loading original {dataset_type} dataset...')
        reader = pd.read_json(readfile, orient='columns', lines=True,
                              encoding='utf-8', chunksize=CHUNK_SIZE)
        print('Done loading dataset.')

        # Drop unneeded data
        total = 0
        for df in reader:
            # Drop non-restaurants in business dataset
            if dataset_type == 'business':
                df = df[df.categories.str.contains('Restaurants', na=False)]

            # Drop unneeded columns and add z-score for this dataset
            df.drop(columns=columns_to_drop[dataset_type], axis=1, inplace=True)
            df['z-score'] = get_z_score_for_type(df, dataset_type)

            # Write to new file and update progress in stdout
            df.to_json(writefile, orient='records', lines=True)
            total += len(df.index)
            print(f'Processed {total} rows', end='\r')

        print(f'Done processing {total} rows in {dataset_type} dataset.')
        print(f'File available at: {outfile_path}')

