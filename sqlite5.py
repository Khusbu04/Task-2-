# Assignment 
import requests
import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import create_engine, Column, Interger, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base = declarative_base()
class Movies(Base):
    __tablename__ = 'movies'
    movie = Column(Integer, primary_key = True)
    genre = Column(String, nullable = False)
    ratings = Column(Float, nullable = False)
    release_date = Column(Integer, primary_key = True)
engine = create_engine('sqlite://')

def fetch_movies():
    base_url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}'
try:
    response = requests.get(base_url)
    movies_data = response.json()

for movie in movies:
    print(movie['title'], movie['genre_ids'], movie['vote_average'], movie['release_date'])
#import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY,
    title TEXT,
    genre_ids TEXT,
    rating REAL,
    release_date TEXT
)
''')

# Insert data into the table
for movie in movies:
    cursor.execute('''
    INSERT INTO movies (title, genre_ids, rating, release_date)
    VALUES (?, ?, ?, ?)
    ''', (movie['title'], str(movie['genre_ids']), movie['vote_average'], movie['release_date']))

conn.commit()
conn.close()
#import pandas as pd
#import numpy as np

# Load data from SQLite database
conn = sqlite3.connect('movies.db')
df = pd.read_sql_query("SELECT * FROM movies", conn)
conn.close()

# Recommendation algorithm based on genre similarity and ratings
def recommend_movies(user_genres, df):
    df['genre_match'] = df['genre_ids'].apply(lambda x: any(genre in x for genre in user_genres))
    df = df[df['genre_match'] == True]
    df = df.sort_values(by='rating', ascending=False)
    return df[['title', 'rating', 'release_date']].head(10)

user_genres = [28, 12]  # Example genre IDs
recommendations = recommend_movies(user_genres, df)
print(recommendations)

# CVS
recommendations.to_csv('recommendations.csv', index=False)


#import matplotlib.pyplot as plt

# Bar chart for top 5 genres
genre_counts = df['genre_ids'].explode().value_counts().head(5)
genre_counts.plot(kind='bar')
plt.title('Top 5 Genres Watched')
plt.xlabel('Genre')
plt.ylabel('Count')
plt.show()

# Pie chart for ratings
rating_counts = df['rating'].value_counts()
rating_counts.plot(kind='pie', autopct='%1.1f%%')
plt.title('Ratings Distribution')
plt.show()

# Line graph for movie releases per year
df['release_year'] = pd.to_datetime(df['release_date']).dt.year
release_trends = df['release_year'].value_counts().sort_index()
release_trends.plot(kind='line')
plt.title('Movie Releases Per Year')
plt.xlabel('Year')
plt.ylabel('Number of Movies')
plt.show()

