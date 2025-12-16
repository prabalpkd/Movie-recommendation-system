# 🎬 Content-Based Movie Recommendation System

A **content-based movie recommendation system** that suggests similar movies by analyzing textual metadata using **Natural Language Processing (NLP)** techniques and **cosine similarity**. This project is designed to work **without user ratings or interaction data**, making it suitable for **cold-start scenarios** and academic demonstrations of recommender system fundamentals.

---

## 📌 Project Overview

Modern streaming platforms rely heavily on recommender systems to help users discover relevant content from massive catalogs. This project implements a **content-based recommender**, where movies are recommended based on their intrinsic attributes rather than user behavior.

The system analyzes movie **overviews, genres, keywords, cast, and crew information**, converts them into numerical feature vectors, and computes similarity scores between movies. Given a movie title, the system returns the **top-K most similar movies**.

---

## 🚀 Key Features

* Fully **content-based filtering** approach
* No dependency on user ratings or historical interactions
* Rich feature engineering using movie metadata
* NLP preprocessing: tokenization, normalization, and stemming
* Bag-of-Words text representation
* Cosine similarity for efficient similarity computation
* Offline evaluation using **Precision@K** and **Recall@K**

---

## 🗂 Dataset

This project uses the **TMDB 5000 Movies Dataset**.

Required files:

* `tmdb_5000_movies.csv`
* `tmdb_5000_credits.csv`

The datasets contain structured movie metadata and cast/crew details. They are merged using the movie title as a common key.

Dataset source: TMDB (via Kaggle)

---

## 🛠️ Technologies & Libraries

* **Python 3.12**
* **Pandas**, **NumPy** – data manipulation
* **NLTK** – text preprocessing and stemming
* **Scikit-learn** – vectorization and similarity computation

---

## ⚙️ System Architecture & Workflow

1. Load and merge movie and credit datasets
2. Parse structured metadata (genres, keywords, cast, crew)
3. Clean and normalize text data
4. Combine features into a unified `tags` column
5. Convert text into numerical vectors using Bag-of-Words
6. Compute pairwise cosine similarity
7. Generate top-K movie recommendations

---

## ▶️ How to Use

### Example

```python
recommend("Avatar")
```

**Sample Output:**

```
Aliens vs Predator: Requiem
Aliens
Falcon Rising
Independence Day
Titan A.E.
```

The function returns movies ranked by similarity to the input title.

---

## 📊 Evaluation Strategy

Traditional accuracy metrics are not applicable to recommender systems. Therefore, ranking-based metrics are used:

* **Precision@K (Primary Metric)**
  Measures the proportion of relevant movies among the top-K recommendations. This aligns closely with real-world user experience, where only a small number of recommendations are displayed.

* **Recall@K (Secondary Metric)**
  Measures the proportion of all relevant movies that appear in the top-K list. Recall is naturally low due to the limited size of K.

**Relevance Definition:**
A recommended movie is considered relevant if it shares at least one genre with the query movie. Genre information is used only for evaluation to avoid feature leakage.

---

## 🖼️ Screenshots

> 📌 *Add screenshots of your application or output here*

```
/screenshots
 ├── recommendation_output.png
 ├── similarity_matrix.png
```

You can include screenshots of:

* Sample recommendations
* Evaluation metrics output
* UI (if deployed using Streamlit)

---

## 🎥 Demo

> 📌 *Add a demo video or GIF here*

* Demo Video: `demo.mp4`
* Demo GIF: `demo.gif`

Suggested demo content:

* Entering a movie title
* Display of recommended movies
* Explanation of similarity scores

---

## 🔮 Future Enhancements

* Replace Bag-of-Words with **TF-IDF** vectorization
* Introduce **hybrid recommendation** (content + collaborative filtering)
* Incorporate user ratings and personalization
* Improve evaluation with MAP@K or NDCG
* Deploy as a web application using **Streamlit** or **Flask**

---

## 📄 License

This project is intended for **academic and educational purposes only**.

---

## 🙌 Acknowledgements

* TMDB for providing the dataset
* Scikit-learn and NLTK open-source communities
