"""
Have you seen the new live action of Snow White? If you haven't seen it, make sure you don't! 😅
It is one of the worst movies ever with a rating of 1.5 on IMDb and it is worse than a rotten tomato.

With this fiasco in mind, let's try to predict how sucessfull a movie can be with this dataset I found on kaggle 
(https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?resource=download).
It contains a list of movies with data regarding plot, cast, crew, budget and revenues.
Can we predict the success of a movie?

This file simulates a simple predict problem. Now, the main objetive of this code is to 
analyse diff changes, add files to the staging area, make a commit and push those changes,
so please don't judge this toy example on how simple this analysis will be (we´re in a github workshop!)

Oh no! This code is full of breakpoints and therefore we cannot run it end to end!
If you don't know what breakpoints are, it is like the pause button on your remote, and the code
won't run unless you intruct it - however it is great for debbugging.

In this pratical exercise your main objetive is to remove the breakpoint() sequencially
and running in the terminal at each step with the command (python/python3 pratical/exercise.py).
Make sure you are in the right place, you should be inside the repository in the directory:
( ../novaims_github_workshop )

In the end you should have no breakpoint() functions!!
"""

### Install required packages ###
import subprocess
import sys

# List of required packages
required_packages = ['pandas', 'scikit-learn', 'matplotlib']

# Install needed packages (if you don't have them)
for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        print(f"Installing missing package: {package}")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])


## Import libraries ##
import random
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Load dataset (make sure you have a 'movies.csv' file)
df_full = pd.read_csv('pratical/data/movies.csv')

# Select only columns we want
columns = ['title', 'budget', 'popularity', 'revenue', 'runtime', 'vote_average']
df = df_full[columns]

# Drop rows with missing or zero values
df = df[(df != 0).all(1)].dropna()

# Lets make a quick analysis of the dataset
# ----------- EXPLORATORY ANALYSIS -----------

# Histogram: Revenue distribution
plt.figure(figsize=(6,4))
plt.hist(df['revenue'] / 1e6, bins=30, edgecolor='black')
plt.title('Count of movies for revenue')
plt.xlabel('Revenue (Millions)')
plt.ylabel('Number of Movies')
plt.grid(True)
plt.tight_layout()
plt.show()

breakpoint()

# Scatter plot: Budget vs Revenue
plt.figure(figsize=(6,4))
plt.scatter(df['budget'] / 1e6, df['revenue'] / 1e6, alpha=0.5)
plt.title('Budget vs Revenue')
plt.xlabel('Budget (Millions)')
plt.ylabel('Revenue (Millions)')
plt.grid(True)
plt.tight_layout()
plt.show()

breakpoint()

# Select relevant features
features = ['budget', 'popularity']
target = 'revenue'


# Create a clean copy for modeling
df_clean = df[features + [target]].dropna()

# Features (X) and target (y)
X = df_clean[features]
y = df_clean[target]

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
print("Model trained!")

breakpoint()

# Feature importances
print("\nFeature Importances:")
for feature, importance in zip(features, model.feature_importances_):
    print(f"  {feature}: {importance:.2f}")

# ----------- PREDICTION ON A REAL MOVIE FROM TEST SET -----------

# Get one random test sample
sample_index = random.choice(X_test.index.tolist())
sample_features = X_test.loc[sample_index]
sample_actual = y_test.loc[sample_index]
sample_title = df.loc[sample_index, 'title']

# Make prediction
sample_df = pd.DataFrame([sample_features])
predicted_revenue = model.predict(sample_df)[0]

breakpoint()

# Show result
print(f"\nMovie: {sample_title}")
print(f"  Budget: ${sample_features['budget']:,.0f}")
print(f"  Popularity: {sample_features['popularity']}")
print(f"  Actual Revenue: ${sample_actual:,.2f}")
print(f"  Predicted Revenue: ${predicted_revenue:,.2f}")

