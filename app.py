import pandas as pd
import streamlit as st
import pickle
import requests
import urllib.parse

st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #1a1a1a 0%, #0f0f3d 100%);
        color: white;
    }

    .stApp {
        background: linear-gradient(135deg, #1a1a1a 0%, #0f0f3d 100%) !important;
    }
    </style>
""", unsafe_allow_html=True)



OMDB_API_KEY = "121355a8"

# -------------------------------
# Fetch Poster from OMDb using TITLE
# -------------------------------
def fetch_poster(movie_title):
    # URL Encode the title to avoid issues with spaces/special characters
    encoded_title = urllib.parse.quote(movie_title)

    url = f"http://www.omdbapi.com/?t={encoded_title}&apikey={OMDB_API_KEY}"
    data = requests.get(url).json()

    poster_url = data.get("Poster")

    # If poster unavailable
    if poster_url is None or poster_url == "N/A":
        return "https://via.placeholder.com/200x300?text=No+Poster"

    return poster_url


# -------------------------------
# Recommendation Function
# -------------------------------
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movies_list:
        title = movies.iloc[i[0]].title
        recommended_movies.append(title)
        recommended_posters.append(fetch_poster(title))

    return recommended_movies, recommended_posters


# -------------------------------
# Load Data
# -------------------------------
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))


# -------------------------------
# Streamlit UI
# -------------------------------
st.title("🎬 Movie Recommender System")

selected_movie_name = st.selectbox(
    "Select your favourite Movie",
    movies['title'].values
)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    cols = st.columns(5)

    for idx, col in enumerate(cols):
        with col:
            st.markdown(f"""
<div class="movie-card">
    <img src="{posters[idx]}" width="170" style="border-radius:10px;">
    <div class="movie-title">{names[idx]}</div>
</div>
""", unsafe_allow_html=True)

