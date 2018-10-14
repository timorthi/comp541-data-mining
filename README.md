# Setup
### Python
1. Install Python 3.6 on your system. You can use `python --version` to make sure you have it installed correctly.
2. Clone this repository and `cd` into it
    ```
    $ git clone git@github.com:timorthi/comp541-data-mining.git && cd comp541-data-mining
    ```
3. Install the python libraries we'll use for this project via `requirements.txt`:
    ```
    $ pip install -r requirements.txt
    ```

### Datasets
1. Download the following datasets:
    * [TripAdvisor Restaurant Data](https://www.kaggle.com/PromptCloudHQ/restaurants-on-tripadvisor#tripadvisor_in-restaurant_sample.csv)
    * [Yelp Dataset](https://www.kaggle.com/yelp-dataset/yelp-dataset)
    * [US Household Income Statistics](https://www.kaggle.com/goldenoakresearch/us-household-income-stats-geo-locations/version/8)
    * [Los Angeles Crime Data](https://catalog.data.gov/dataset/crime-data-from-2010-to-present/resource/3762201e-a641-4be5-ba56-2eb0f6cd2b0f)
2. Make a folder called `datasets`, move the files in there, and unzip them. This folder is ignored by git, so don't worry about committing it. If we all have a `datasets` folder then we can write general scripts and run them without too much configuration.

# Development Workflow
* The master branch represents the most recently updated version of our code.
* When working on something new, always create a new branch and work on that branch, opening a pull request to merge back into `master` when you're done.

## Fetching changes
If someone else has pushed their changes to the remote repository and it's been merged into master, you'll want to update your local repository:
1. Make sure you're on the master branch:
    ```
    $ git checkout master
    ```
2. Pull from the remote:
    ```
    $ git pull origin master
    ```

## Pushing your changes
1. If you're working on something, be sure to start your work on a new branch with a descriptive branch name like:
    ```
    $ git checkout -b yelp_dataset_preprocessing
    ```
2. As you're completing parts of your feature, commit your work as needed:
    ```
    $ git add .
    $ git commit -m "Cleaned up reviews file"
    ```
3. When you're done with whatever you're working on, push to the remote GitHub repository
    ```
    $ git push
    ```
* [Create a pull request](https://help.github.com/articles/creating-a-pull-request/) on GitHub and have us review it so we can merge it to the master branch

