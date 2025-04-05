# Movie Recommender System

![image](https://github.com/user-attachments/assets/deb8916b-2be2-4bb6-b148-a2e40df0cde9)
![image](https://github.com/user-attachments/assets/f9689f02-b8e1-4f2f-aa76-8cd03c020b29)
![image](https://github.com/user-attachments/assets/cd8b53db-2e1e-43d1-91fd-da0a6745ea04)

## Overview

This project implements a **Movie Recommender System** using machine learning techniques to suggest movies based on a selected movie. The system utilizes **Cosine Similarity** to find similar movies based on their features. The project also integrates the **The Movie Database API (TMDb)** to fetch movie posters dynamically.

The recommender system has a web-based interface built using **Streamlit**, allowing users to interact with the application, select a movie, and receive movie recommendations with posters.

## Features

- **Movie Selection**: The user can type or select a movie from a dropdown list.
- **Movie Recommendations**: The system returns the top 5 most similar movies based on the selected movie.
- **Movie Posters**: Displays movie posters fetched dynamically from The Movie Database API.
- **Interactive Web Interface**: The UI is built using **Streamlit**, providing an interactive user experience.
- **Model Training**: The movie recommendation model is based on **Cosine Similarity** and **Content-Based Filtering**.

## Technologies Used

- **Streamlit**: For building the interactive web interface.
- **Pandas**: For data manipulation and analysis.
- **NumPy**: For handling large data arrays.
- **Scikit-learn**: For machine learning, including preprocessing, feature extraction, and similarity computation.
- **Requests**: For API calls to **TMDb**.
- **Plotly**: For any future visualizations (if needed).
- **NLTK**: For text processing and stemming (if text data is involved).
- **Matplotlib/Seaborn**: For data visualization.

## Installation

### Prerequisites

- Python 3.6 or higher
- Required Python libraries (listed below)

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/movie-recommender-system.git
cd movie-recommender-system






