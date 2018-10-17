import pandas

ENCODING = 'utf-8'
DATASETS_FOLDER_PATH = '../datasets'

dataset_paths = {
    'user': f'{DATASETS_FOLDER_PATH}/yelp_user_processed.csv',
    'review': f'{DATASETS_FOLDER_PATH}/yelp_review_processed.csv',
    'business': f'{DATASETS_FOLDER_PATH}/yelp_business_processed.csv'
}
outfile_path = f'{DATASETS_FOLDER_PATH}/yelp_integrated.csv'


with open(dataset_paths['business'], encoding=ENCODING) as business_file, \
     open(dataset_paths['user'], encoding=ENCODING) as user_file, \
     open(dataset_paths['review'], encoding=ENCODING) as review_file, \
     open(outfile_path, 'w') as outfile:

    print('Loading processed yelp datasets into memory...')
    business_df = pandas.read_csv(business_file, index_col=0) # Index on business_id
    print(f'Loaded business dataframe with {len(business_df.index)} records')

    user_df = pandas.read_csv(user_file, index_col=1) # Index on user_id
    user_df = user_df[~user_df.index.duplicated(keep='first')] # Drop repeats of the same user_id
    print(f'Loaded user dataframe with {len(user_df.index)} records')

    review_df = pandas.read_csv(review_file)
    print(f'Loaded review dataframe with {len(review_df.index)} records')


    print('Joining dataframes...')
    # Join user and review dataframes on user_id column
    user_review_df = user_df.merge(review_df,
                                   on='user_id',
                                   suffixes=('_user', '_review'),
                                   validate='one_to_many')
    print(f'Merged user and review dataframes into UserReview ({len(user_review_df.index)} records)')

    # Join business and user_review dataframes on business_id column, set index, and clear rows with empty fields
    business_review_df = business_df.merge(user_review_df,
                                           left_index=True,
                                           right_on='business_id',
                                           suffixes=('_business', '_review'),
                                           validate='many_to_many') \
                                    .set_index('business_id')
    print(f'Merged business and UserReview dataframes ({len(business_review_df.index)} records)')

    print('Writing to file...')
    business_review_df.to_csv(outfile)
    print(f'Saved merged dataframe to {outfile_path}')

print('Done!')
