import pandas as pd
import numpy as np
import seaborn as sns
import os
import json
import requests

from dotenv import load_dotenv
load_dotenv()


def echo(x):
    return str(x)


def say_hello():
    print('hello')


def download_dataset():
    """Downloads a dataset from kaggle and only keeps the csv in your data file.
    Takes: url from kaggle
    Returns: a folder with the downloaded and unzipped csv
    """
    # Gets the name of the dataset.zip
    url = 'https://www.kaggle.com/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows'

    # Gets the name of the dataset.zip
    endopint = url.split("/")[-1]
    user = url.split("/")[-2]

    # Download, decompress and leaves only the csv
    download = f"kaggle datasets download -d {user}/{endopint}"
    decompress = f"tar -xzvf {endopint}.zip"
    delete = f"del -F {endopint}.zip"

    for i in [download, decompress, delete]:
        os.system(i)

    # Move the csv to your data folder
    move_and_delete = f"move *.csv ..\\csv_data\\dataset.csv"
    return os.system(move_and_delete)


def drop_column(data, column):
    """Delete column
    Takes: dataframe, dataframe column list
    Returns: dataframe without the indicated columns
    """
    return data.drop(column, axis=1)


def get_original_language(row):
    """API call to get original language information
    Takes: cell with movie title
    Returns: original language opted from API information
    """

    title1 = row['Series_Title'].replace(" ", "+")
    api_key = os.getenv("toke")
    response = requests.get('https://api.themoviedb.org/3/search/movie?api_key=' + api_key + '&query=' + title1).json()
    # print(json.dumps(response, indent=4, sort_keys=True))
    # print(response['results'])
    for result in response['results']:
        if result['title'] == row['Series_Title']:
            return result['original_language']
    return '-'


def apply_original_language(data):
    """Create new column to indicate the result of get_original_language
    Takes: dataframe
    Returns: cell with original language opted from API information
    """
    return data.apply(get_original_language, axis=1)


def main():
    pass


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    main()


