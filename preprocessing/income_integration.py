import pandas

ENCODING = 'utf-8'
DATASETS_FOLDER_PATH = '../datasets'

dataset_paths = {
    'yelp_integrated': f'{DATASETS_FOLDER_PATH}/yelp_integrated.csv',
    'income': f'{DATASETS_FOLDER_PATH}/us_income_kaggle_processed.csv',
}
outfile_path = f'{DATASETS_FOLDER_PATH}/final_integrated_data.csv'

with open(dataset_paths['yelp_integrated'], encoding=ENCODING) as yelp_file, \
    open(dataset_paths['income'], encoding=ENCODING) as income_file, \
    open(outfile_path, 'w') as outfile:

    print('Loading integrated Yelp dataset and preprocessed income dataset into memory...')
    yelp_df = pandas.read_csv(yelp_file,
                              low_memory=False,
                              dtype={'postal_code': 'object'})
    yelp_df.dropna(inplace=True)
    print(f'Loaded yelp dataframe with {len(yelp_df.index)} records')

    income_df = pandas.read_csv(income_file,
                                index_col=0,
                                dtype={'Zip_Code': 'object'})
    income_df.dropna(inplace=True)
    income_df.drop_duplicates(subset='Zip_Code', keep='first', inplace=True)
    print(f'Loaded income dataframe with {len(income_df.index)} records')

    print('Merging dataframes...')
    yelp_income_df = yelp_df.merge(income_df,
                                   left_on='postal_code',
                                   right_on='Zip_Code')
    print(f'Merged Yelp and Income dataframes ({len(yelp_income_df.index)} records)')

    print('Writing to file...')
    yelp_income_df.to_csv(outfile, index=False)
    print(f'Saved merged dataframe to {outfile_path}')

print('Done!')
