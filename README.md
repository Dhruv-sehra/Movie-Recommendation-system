<h2>🎬 Movie Recommender System</h2>
An AI-powered Discovery Engine with a Custom Network Bypass
This project is a full-stack Content-Based Movie Recommendation System. It leverages Machine Learning to analyze movie metadata and suggests similar titles based on a user's selection. A unique feature of this project is the implementation of a Custom Cloudflare Proxy to ensure 100% API uptime by bypassing regional ISP restrictions.

<h2>🚀 Key Features</h2>
Vectorized Search: Uses NLP techniques to convert movie tags into high-dimensional vectors.

Cosine Similarity: Employs mathematical distance measurements to find the "closest" movies to your favorites.

Live Metadata: Fetches real-time posters and movie details via the TMDB API.

ISP-Resilient Architecture: Includes a custom-built Cloudflare Worker proxy to handle API requests, solving common ConnectionTimeout issues in restricted regions.

<h2>🛠️ Tech Stack</h2>
<b>Language:</b> Python 3.11

<b>Machine Learning:</b> Scikit-learn (CountVectorizer, Cosine Similarity), NLTK (PorterStemmer)

<b>Frontend:</b> Streamlit

<b>Data Handling:</b> Pandas, NumPy, Pickle

<b>DevOps/Networking:</b> Cloudflare Workers (JavaScript Proxy), Dotenv

<h2>🧠 How It Works</h2>
<b>1. Data Preprocessing</b>
The model processes the TMDB 5000 Movie Dataset. We extract key features like genres, keywords, cast (top 3), and crew (Director).

Stemming: Words like "loving," "loved," and "love" are converted to the root word "love" using PorterStemmer to ensure better matching.

Vectorization: We convert the combined "tags" for each movie into a 5,000-word vector using CountVectorizer.

<b>2. The Recommendation Logic</b>
When a user selects a movie, the system calculates the Cosine Similarity between that movie's vector and every other movie in the database. It then returns the top 5 most similar titles.

<b>3. Custom API Gateway</b>
To solve the ERR_CONNECTION_TIMED_OUT error common with TMDB in certain regions, I deployed a middleman proxy using Cloudflare Workers. This ensures the Python script always has a stable connection to the metadata server.


<h2>📦 Installation & Setup:</h2>
  <b>1. Clone the Repo:</b>
  
         git clone https://github.com/your-username/movie-recommender.git
         cd movie-recommender

  <b>2. Environment Variables:</b>
     Create a .env file in the root directory and add your TMDB credentials:

         TMDB_API_KEY=your_api_key_here
         TMDB_BASE_URL=https://your-cloudflare-proxy.workers.dev/3
  <b>3. Install Dependencies:</b>
  
          pip install -r requirements.txt
  4. Download the TMDB 5000 Movie Dataset <a>https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata </a> from Kaggle and place tmdb_5000_movies.csv and tmdb_5000_credits.csv in the root folder.


  <b>5. Run the App:</b>

          streamlit run app.py



<h2>👨‍💻 Author</h2>
Dhruv Sehra B.Tech AI/ML Student
