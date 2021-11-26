import pandas as pd
import streamlit as st
import pickle
import pandas as pd
import requests

movie_dict = pickle.load(open('movie_dict3.pkl','rb'))
similarity = pickle.load(open('similarity3.pkl','rb'))
movies = pd.DataFrame(movie_dict)

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=13faf3e6c935ed456f46114a4cbd0b45'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:6]

    recommend_movies = []
    recommend_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_movies_poster.append(fetch_poster(movie_id))
    return recommend_movies,recommend_movies_poster

st.title('Movie Recomendation System')

selected_movie = st.selectbox(
'Select Movie',
movies['title'].values)

if st.button('Recomended'):
    names,poster = recommend(selected_movie)
    col1, col2, col3,col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])

    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])
