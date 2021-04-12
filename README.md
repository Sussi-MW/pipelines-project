
<img src="https://github.com/Sussi-MW/pipelines-project/blob/master/Portada.jpg" width="500" height="200">

# Project: Data Pipeline
## by Susana Martin Wanton

## Goal:

The goal of this project is to make an executable file that grant the combined analysis of a selected data set enriched with the search for information from related APIs. The pipeline is based on the definition of functions that allow importing a data set and using data management skills to clean it and prepare it for analysis.

---

## **Hypothesis**

Most of the movies that are in the top 1000 IMDB_Rating have English original language.

---

## Procedure:

### Start up

```bash
1-(downloading-and-cleaning.py)
2-(enriching-and-cleaning.ipynb)
```

- Function that downloads and imports the data set from kaggle.com

- Data set loading and analysis.

**Cleaning and reorganizing the dataset:**
- Function that removes all columns that are not needed.
- Look for null values.

**Enriching the dataset with external data:**
- Function that calls the API to obtain information related to the original language.
- Set of functions that show the results obtained in a new column called 'Original language'

Export the new data set.

### Visualizing

```bash
3-(visualizing.ipynb)
```
- Rating analysis graph. Show mean and median.
- Quantitative analysis graph of the original language.
- Histogram of linkage analysis between Rating and original language.

---
## Resources used

* [Python Functional Programming How To Documentation](https://docs.python.org/3.7/howto/functional.html)
* [Python Errors and Exceptions Documentation](https://docs.python.org/3/tutorial/errors.html)
* [StackOverflow String Operation Questions](https://stackoverflow.com/questions/tagged/string+python)
* [Kaggle Data Sets](https://www.kaggle.com/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows?select=imdb_top_1000.csv)
* [API](https://www.themoviedb.org/)
