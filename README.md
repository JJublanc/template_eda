# Descriptions
Comparison of several EDA (Exploratory Data Analysis) solutions.

# Settings
Set your virtual or conda environment, activate it and set a Ipython kernel associeted with it.

```
python -m venv env
source venv/bin/activate
pip install -r requirements.txt
```

# Get data
Before using Kaggle API, make sure you have a Kaggle account and an API key dowloaded from Kaggle 
to ~/.kaggle/kaggle.json.

Then install Kaggle package.
```
pip install kaggle
```

### Pokemon dataset
```
kaggle datasets download -d jackbydalek/pokemon-with-stats-with-gen-7
unzip pokemon-with-stats-with-gen-7.zip -d data/
```

### Image dataset
```
kaggle datasets download -d eisgandar/pangolins
unzip pangolins.zip -d data/pangolins/
```

clean data and keep only .jpeg files
1/ First make sure you are in the goo folder.
```
cd data/pangolins/
```
Then list the file to delete
```
ls | grep -v *.jpg 
```

And finally delete the files
```
ls | grep -v *.jpg | xargs rm
```

Finally, come back to root folder and clean zip file.
```
cd ../..
rm pangolins.zip
```

### Tweets dataset
```
kaggle datasets download -d dshah1612/product-tweets-dataset
unzip product-tweets-dataset.zip -d data/tweets/
rm product-tweets-dataset.zip
```

# Launch pandas profiling
```
python src/pandas_profiling_pokemon.py
python src/pandas_profiling_tweets.py
```

# Launch SweetViz
```
python src/sweetviz_pokemon.py
```

# Explore images data (custom)
```
python src/pangolins_custom.py 
```

# Explore tweets (custom)
```
python src/tweets_custom.py
```

