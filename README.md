# 🎬 Content-Based Movie Recommendation System

## 📌 Project Description:
This project implements an **end-to-end Content-Based Movie Recommendation System** using **Natural Language Processing (NLP)** techniques.  
The system recommends movies based on **similarity between movie content**, such as plot overview, genres, keywords, cast, and director.

The goal is to build a **scalable, explainable, and production-aware recommendation engine** that does **not rely on user interaction data**, making it suitable for cold-start scenarios.

---

## 🧠 What Is Content-Based Recommendation?
A content-based recommendation system suggests items that are **similar to a given item**, based on their attributes.

> If a user likes a particular movie, the system recommends other movies with similar content.

This approach is especially useful when:
- User history is unavailable
- The system is new
- Explainability is important

---
## 🎥 Demo

* Check out the live Streamlit app here: [Movie_Recommender_System](https://movie-recommendation-system-c2s7xfl8mjczzwztdwbudy.streamlit.app/)
* ![App Screenshot](https://github.com/prabalpkd/Movie-recommendation-system/blob/main/Snapshot-03.png)

---

## 📂 Dataset Information
The project uses the **TMDB 5000 Movies Dataset**, which contains metadata for ~5000 movies.

### Files Used
- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

### Important Columns
| Column | Description |
|------|-------------|
| movie_id | Unique identifier for a movie |
| title | Movie title |
| overview | Short plot summary |
| genres | List of genres |
| keywords | Thematic keywords |
| cast | Actors involved in the movie |
| crew | Crew members (director extracted) |

> ⚠️ Note: Several columns are stored as **stringified lists/dictionaries**, which are parsed during preprocessing.

---

## ⚙️ Technology Stack
- **Programming Language:** Python  
- **Libraries:**  
  - Pandas, NumPy  
  - NLTK (Porter Stemmer)  
  - Scikit-learn  
- **Techniques:**  
  - Bag of Words  
  - Cosine Similarity  
- **Tools:**  
  - Jupyter Notebook  
  - Pickle (serialization)

---

## 🏗️ System Architecture
```
Raw Movie Data (CSV)
↓
Data Cleaning & Validation
↓
Feature Extraction
↓
Text Normalization & Stemming
↓
Feature Engineering (Tags)
↓
Text Vectorization (BoW)
↓
Similarity Computation
↓
Recommendation Engine
↓
Evaluation (Precision@K)
↓
Serialized Artifacts (Deployment)
```

---

## 🧹 Data Cleaning & Preprocessing

### 1. Dataset Merging
The movie metadata and credits datasets are merged using the `title` column to combine content and cast/crew information.

### 2. Missing Value Handling
- Rows with missing values are dropped.
- Ensures consistency in feature extraction and vectorization.

### 3. Duplicate Handling
- Duplicate records are checked to avoid biased similarity calculations.

---

## 🏷️ Feature Engineering (Core Step)

### Selected Features
Only content-relevant columns are used for modeling:
- movie_id, title, overview, genres, keywords, cast, crew
---


### Feature Extraction Logic
- **Genres & Keywords:** Extract only the `name` field
- **Cast:** Top 3 actors (most influential)
- **Crew:** Director only
- **Overview:** Tokenized into words

### Why These Features?
These attributes best represent the **semantic meaning** of a movie and are highly effective for content similarity.

---

## 🧩 Tags Creation
All extracted features are combined into a single column called `tags`.

```tags = overview + genres + keywords + cast + director```


- This column acts as a **textual representation of each movie**.


---

## ✂️ Text Normalization
To improve model performance and reduce noise:

- Converted text to lowercase
- Removed spaces in multi-word names (e.g., "Science Fiction" → "ScienceFiction")
- Applied **Porter Stemming**


This reduces vocabulary size and improves similarity matching.

---

## 🔢 Text Vectorization
The `tags` text is converted into numerical form using:

### Bag of Words (CountVectorizer)
- Maximum features: **5000**
- English stopwords removed

Output:
(number_of_movies × 5000) sparse matrix

Each row represents a movie, and each column represents a word frequency.

---

## 📐 Similarity Computation
### Cosine Similarity
Cosine similarity measures the **angle between two vectors**, indicating how similar two movies are.

- Range: 0 (no similarity) to 1 (identical)
- Produces a **square similarity matrix**

This matrix is the backbone of the recommendation engine.

---

## 🎯 Recommendation Logic
### Workflow
1. User selects a movie
2. System retrieves the movie’s vector
3. Computes similarity with all other movies
4. Sorts movies by similarity score
5. Returns top-N recommendations (excluding itself)

Example:
```python
recommend("Spectre")
```
---

📊 Model Evaluation
Metric: Precision@K

Precision@K evaluates recommendation quality by answering:

Out of the top K recommended movies, how many are relevant?

Relevance Definition

A recommended movie is considered relevant if:

It shares at least one genre with the target movie

---
💾 Model Serialization & Deployment Readiness

To enable deployment and reuse, the following artifacts are saved using Pickle:

| File              | Description                    |
| ----------------- | ------------------------------ |
| `movies_dict.pkl` | Dictionary format for web apps |
| `similarity.pkl`  | Precomputed similarity matrix  |

These files can be directly loaded into:

- Streamlit apps

- Flask/Django APIs

---
## 🔮 Future Enhancements

* Replace Bag-of-Words with **TF-IDF** vectorization
* Introduce **hybrid recommendation** (content + collaborative filtering)
* Incorporate user ratings and personalization
* Improve evaluation with MAP@K or NDCG
* Deploy as a web application using **Streamlit** or **Flask**

---

##🧑‍💻 Author

- Prabal
- Aspiring Data Scientist
- Skilled in Machine Learning, NLP, Deep Learning & Recommendation Systems

---

## 🙌 Acknowledgements

* TMDB for providing the dataset
* Scikit-learn and NLTK open-source communities

