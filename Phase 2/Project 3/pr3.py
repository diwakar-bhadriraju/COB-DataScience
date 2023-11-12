import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset into a Pandas DataFrame
df = pd.read_csv('netflix.csv')

# Display the first few rows of the dataset to understand its structure
print(df.head())

# Step 1: Basic dataset exploration
# Check the distribution of release years
plt.figure(figsize=(12, 6))
sns.histplot(df['release_year'], bins=30, kde=True)
plt.title('Distribution of Release Years')
plt.xlabel('Release Year')
plt.ylabel('Frequency')
plt.show()

# Step 2: Explore the distribution of types (Movie/TV Show)
plt.figure(figsize=(8, 5))
sns.countplot(x='type', data=df)
plt.title('Distribution of Show Types (Movie/TV Show)')
plt.xlabel('Show Type')
plt.ylabel('Count')
plt.show()

# Step 3: Explore the distribution of ratings
plt.figure(figsize=(12, 6))
sns.countplot(x='rating', data=df, order=df['rating'].value_counts().index)
plt.title('Distribution of Ratings')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.show()

# Step 4: Explore the distribution of countries
plt.figure(figsize=(16, 8))
sns.countplot(x='country', data=df, order=df['country'].value_counts().index[:10])
plt.title('Top 10 Countries with Most Shows')
plt.xlabel('Country')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.show()

# Step 5: Explore the duration distribution for movies
plt.figure(figsize=(12, 6))
sns.histplot(df[df['type'] == 'Movie']['duration'], bins=30, kde=True)
plt.title('Distribution of Movie Durations')
plt.xlabel('Duration (minutes)')
plt.ylabel('Frequency')
plt.show()

# Step 6: Explore the distribution of genres for TV Shows
plt.figure(figsize=(16, 8))
tv_show_genres = df[df['type'] == 'TV Show']['listed_in'].str.split(', ', expand=True).stack().value_counts()
sns.barplot(x=tv_show_genres.values, y=tv_show_genres.index[:10], orient='h')
plt.title('Top 10 Genres for TV Shows')
plt.xlabel('Count')
plt.ylabel('Genre')
plt.show()
