# BestCat4U-Py
Rewritten version of my '[BestCat4U](https://github.com/tristanvong/BestCat4U)' project using Flask.

## Run the project:
```
docker compose up
```

## How the project is designed:
This project consists of a quiz which uses a weighted approach. Each cat entry in the file `cat_data.py`
or rather dictionary in this list has an integer value (except `hair_length`) this integer is used to
give weight to each trait of the cat.

In `app.py` there is a function `score_cat` which goes over each cat trait and multiplies it with either
1 or 0 based on the user's input/preference. Except for `hair_length` where if user preference is equal
to cat trait then it gets the value of 1 otherwise 0.
