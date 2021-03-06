# Preprocessing
Preprocessing and integration scripts go in this directory.

## Running The Scripts Against Your Local Datasets
1. Make sure you have all the original datasets in the `datasets` folder.
2. If your local dataset filenames don't match the ones specified in the scripts, just change the scripts to point to the correct path for the original dataset files, but don't change the output file names. **Don't commit these changes to GitHub**.
3. `cd` into this folder from the root directory:
```bash
$ cd preprocessing
```
4. Run the preprocessing driver script:
```bash
$ python preprocess_all.py
```
You should see the following files added in the `datasets` folder:
```
yelp_business_processed.csv
yelp_review_processed.csv
yelp_user_processed.csv
us_income_kaggle_processed.csv
tripadvisor_data_processed_USA.csv
Crime_Data_from_2010_to_Present_processed.csv
```

5. After preprocessing is successful, run the integration driver script:
```bash
$ python integrate_all.py
```
You should see the following files added in the `datasets` folder:
```
yelp_integrated.csv
final_integrated_data.csv
```


#### `final_integrated_data.csv` contains information that has been joined on the appropriate columns from the _Yelp Review_, _Yelp User_, _Yelp Business_, and _US Household Income_ datasets.
#### Each row in this final dataset represents a different review/rating for the given business_id, along with the user's information and US household income information for the business' ZIP code.
