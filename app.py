#Using the movies_dict to get the movie titles instead of using a DataFrame. This is because we have stored the movies in a dictionary format and we can access the movie titles using the keys. The rest of the code remains the same as it is still using the similarity matrix to recommend movies based on the user's input.
import streamlit as st
import os
from dotenv import load_dotenv
import pickle
import requests

load_dotenv()

base_url = os.getenv("TMDB_BASE_URL")
api_key = os.getenv("TMDB_API_KEY")

movies_dict = pickle.load(open("movies_dict.pkl","rb"))
movies = movies_dict["title"].values()
similarity = pickle.load(open("similarity.pkl","rb"))
st.title("Movie Recommender System")
st.write("This is a simple movie recommender system built using Streamlit and Python. It uses a precomputed similarity matrix to recommend movies based on the user's input.")
Selected_movie = st.selectbox(
    "Select a movie from the dropdown to get recommendations:",
    movies
)


def fetch_poster(movie_id):
    response = requests.get(f"{base_url}/movie/{movie_id}?api_key={api_key}")
    data = response.json()
    return "http://image.tmdb.org/t/p/w500/" + data["poster_path"]


def recommend(movie):
    for key,title in movies_dict["title"].items():
        if title == movie:
            movie_index = key
            break
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommendations = []
    recommendation_posters = []
    for i in movies_list:
        movie_id = movies_dict["movie_id"][i[0]]
        recommendation_posters.append(fetch_poster(movie_id))
        recommendations.append(movies_dict["title"][i[0]])
         
    return recommendations, recommendation_posters


if st.button("Recommend"):
    recommendations, posters = recommend(Selected_movie)
    st.write("Here are some movies you might like:")
    # for rec in recommendations:
    #     st.write(rec)
    col = st.columns(5)
    for i in range(len(recommendations)):
        with col[i]:
            st.image(posters[i])
            st.write(recommendations[i])


#Using Dataframe to get the movie titles instead of using a dictionary. This is because we have stored the movies in a DataFrame format and we can access the movie titles using the index. The rest of the code remains the same as it is still using the similarity matrix to recommend movies based on the user's input.

# import pandas as pd

# movies_dict = pickle.load(open("movies_dict.pkl","rb"))
# movies = pd.DataFrame(movies_dict)
# similarity = pickle.load(open("similarity.pkl","rb"))
# st.title("Movie Recommender System")
# st.write("This is a simple movie recommender system built using Streamlit and Python. It uses a precomputed similarity matrix to recommend movies based on the user's input.")
# Selected_movie = st.selectbox(
#     "Select a movie from the dropdown to get recommendations:",
#     movies["title"].values
# )


# def recommend(movie):
#     movie_index = movies[movies["title"]==movie].index[0]
#     distances = similarity[movie_index]
#     movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
#     recommendations = []
#     for i in movies_list:
#         recommendations.append(movies.iloc[i[0]].title)
#     return recommendations


# if st.button("Recommend"):
#     recommendations = recommend(Selected_movie)
#     st.write("Here are some movies you might like:")
#     for rec in recommendations:
#         st.write(rec)
    # col1,col2,col3,col4,col5=st.columns(5)
    # with col1:
    #     st.image(posters[0])
    #     st.write(recommendations[0])
    # with col2:
    #     st.image(posters[1])
    #     st.write(recommendations[1])

    # with col3:
    #     st.image(posters[2])
    #     st.write(recommendations[2])

    # with col4:
    #     st.image(posters[3])
    #     st.write(recommendations[3])

    # with col5:
    #     st.image(posters[4])
    #     st.write(recommendations[4])