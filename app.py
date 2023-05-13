import streamlit as st
import pickle
import pandas as pd

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
movies = pd.DataFrame(movies_dict)

def recommend(movie):
    movie_index = movies[movies['original_title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommended_movies=[]
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].original_title)
    return recommended_movies

st.title('Movie Recommending System')

selected_movie_name = st.selectbox('Enter The Movie Name to Recommend',movies['original_title'].values)

if st.button('Recommend'):
    recommendations=recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)