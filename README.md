🎬 Movie Recommender System
An AI-powered Discovery Engine with a Custom Network Bypass
This project is a full-stack Content-Based Movie Recommendation System. It leverages Machine Learning to analyze movie metadata and suggests similar titles based on a user's selection. A unique feature of this project is the implementation of a Custom Cloudflare Proxy to ensure 100% API uptime by bypassing regional ISP restrictions.

🚀 Key Features
Vectorized Search: Uses NLP techniques to convert movie tags into high-dimensional vectors.

Cosine Similarity: Employs mathematical distance measurements to find the "closest" movies to your favorites.

Live Metadata: Fetches real-time posters and movie details via the TMDB API.

ISP-Resilient Architecture: Includes a custom-built Cloudflare Worker proxy to handle API requests, solving common ConnectionTimeout issues in restricted regions.

🛠️ Tech Stack
Language: Python 3.11

Machine Learning: Scikit-learn (CountVectorizer, Cosine Similarity), NLTK (PorterStemmer)

Frontend: Streamlit

Data Handling: Pandas, NumPy, Pickle

DevOps/Networking: Cloudflare Workers (JavaScript Proxy), Dotenv

🧠 How It Works
1. Data Preprocessing
The model processes the TMDB 5000 Movie Dataset. We extract key features like genres, keywords, cast (top 3), and crew (Director).

Stemming: Words like "loving," "loved," and "love" are converted to the root word "love" using PorterStemmer to ensure better matching.

Vectorization: We convert the combined "tags" for each movie into a 5,000-word vector using CountVectorizer.

2. The Recommendation Logic
When a user selects a movie, the system calculates the Cosine Similarity between that movie's vector and every other movie in the database. It then returns the top 5 most similar titles.

3. Custom API Gateway
To solve the ERR_CONNECTION_TIMED_OUT error common with TMDB in certain regions, I deployed a middleman proxy using Cloudflare Workers. This ensures the Python script always has a stable connection to the metadata server.


📦 Installation & Setup:
  1. Clone the Repo:
  
         git clone https://github.com/your-username/movie-recommender.git
         cd movie-recommender

  2. Environment Variables:
     Create a .env file in the root directory and add your TMDB credentials:

         TMDB_API_KEY=your_api_key_here
         TMDB_BASE_URL=https://your-cloudflare-proxy.workers.dev/3
  3. Install Dependencies:
  
          pip install -r requirements.txt
  4. Download the TMDB 5000 Movie Dataset <a>https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata </a> from Kaggle and place tmdb_5000_movies.csv and tmdb_5000_credits.csv in the root folder.
  5. Run the App:

          streamlit run app.py



👨‍💻 Author
Dhruv Sehra B.Tech AI/ML Student
