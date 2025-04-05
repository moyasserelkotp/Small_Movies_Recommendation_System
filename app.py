import streamlit as st
import pickle
import requests

# ========== CONFIG ========== #
st.set_page_config(page_title="Movie Recommender", layout="wide")

# ========== HEADER ========== #
st.markdown(
    """
    <h1 style='text-align: center; color: #6C63FF;'>🎬 Movie Recommender System</h1>
    <p style='text-align: center;'>Select a movie and get similar recommendations with posters!</p>
""",
    unsafe_allow_html=True,
)


# ========== FETCH POSTER FUNCTION ========== #
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=c4b76d5deff8af9434b07dde68c7c158&language=en-US"
        response = requests.get(url).json()
        poster_path = response.get("poster_path")
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"
    except:
        return None
    return "https://via.placeholder.com/300x450?text=No+Image"


# ========== RECOMMEND FUNCTION ========== #
def recommend(movie):
    index = movies[movies["title"] == movie].index[0]
    distances = sorted(
        list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1]
    )
    recommended_movies = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        poster = fetch_poster(movie_id)
        recommended_movies.append({"title": movies.iloc[i[0]].title, "poster": poster})
    return recommended_movies


# ========== LOAD MODEL ========== #
movies = pickle.load(open("model/movie_list.pkl", "rb"))
similarity = pickle.load(open("model/similarity.pkl", "rb"))
movie_list = movies["title"].values

# ========== MOVIE SELECTOR ========== #
selected_movie = st.selectbox(
    "🎥 Type or select a movie from the dropdown", movie_list, index=0
)

# ========== SHOW RECOMMENDATION BUTTON ========== #
if st.button("🔍 Show Recommendations"):
    with st.spinner("Finding similar movies..."):
        recommended_movies = recommend(selected_movie)

    st.markdown("---")
    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            st.image(recommended_movies[i]["poster"], use_container_width=True)
            st.markdown(f"**{recommended_movies[i]['title']}**", unsafe_allow_html=True)
