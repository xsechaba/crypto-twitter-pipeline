# Crypto Twitter Data Pipeline

Project Overview

The **Crypto Twitter Data Pipeline** is an automated solution to extract, clean, store, and analyze data from Twitter related to cryptocurrency topics, specifically targeting meme coins, moonshots, and other trending tokens. The objective is to identify trending cryptocurrencies and their sentiment, using the collected data to discover potential high-growth tokens.

The data pipeline utilizes the Twitter API (via RapidAPI) to extract tweets, applies data cleaning and sentiment analysis, and stores the cleaned data for further analysis, including hashtag frequency and trending coin analysis. The pipeline is orchestrated by Apache Airflow for scheduled execution.

# Project Structure

The project contains the following major components:

- **Scripts**
  - `extract_tweets.py`: Extracts cryptocurrency-related tweets from Twitter via the RapidAPI service.
  - `clean_tweets.py`: Cleans the extracted tweets by removing unwanted characters and extracting key information.
  - `store_tweets.py`: Stores cleaned tweets into a database for further analysis.
  - `analyze_trends.py`: Analyzes the hashtag frequency and identifies trending coins.
- **Docker Setup**
  - The project uses Docker to set up a consistent environment for running Airflow and the PostgreSQL database.
- **Apache Airflow DAG**
  - The DAG, `crypto_twitter_dag.py`, schedules the execution of the pipeline in multiple stages to maintain a clean separation of concerns.

# Setup Instructions

Prerequisites

- Docker and Docker Compose
- Python 3.7+
- Git

Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/xsechaba/crypto-twitter-pipeline.git
   cd crypto-twitter-pipeline
   ```

2. **Create a `.env` File**

   Create a `.env` file in the root directory to store sensitive information like your API keys:

   ```
   RAPIDAPI_KEY=your_rapidapi_key
   FERNET_KEY=your_fernet_key
   ```

3. **Start Docker Containers**

   Use Docker Compose to build and start the Airflow and PostgreSQL containers.

   ```bash
   docker-compose up -d
   ```

4. **Access Airflow**

   - Access the Airflow UI by navigating to [http://localhost:8080](http://localhost:8080) in your browser.
   - Log in using the credentials specified during setup (default: username `admin`, password `admin`).

5. **Run the DAG**

   - Enable and trigger the `crypto_twitter_dag` in the Airflow UI.

# Project Workflow

1. **Extract Tweets**

   - `extract_tweets.py` collects relevant cryptocurrency tweets using RapidAPI.
   - The data is saved to a CSV file for the next stage.

2. **Clean Tweets**

   - `clean_tweets.py` processes the raw data, removing special characters and performing sentiment analysis.
   - Cleaned data is saved to a CSV file.

3. **Store Data**

   - `store_tweets.py` saves the cleaned data into a PostgreSQL database.

4. **Analyze Trends**

   - `analyze_trends.py` performs analysis on hashtags and identifies trending coins.
   - The analysis results are saved as CSV files.
   
# Files to Include in GitHub

- **DAGs**: `dags/crypto_twitter_dag.py`
- **Scripts**:
  - `scripts/extract_tweets.py`
  - `scripts/clean_tweets.py`
  - `scripts/store_tweets.py`
  - `scripts/analyze_trends.py`
- **Docker Compose**: `docker-compose.yml`
- **.gitignore**: Excludes `postgres-data/` and sensitive files
- **README.md**: Project overview and setup instructions

# Environment Variables

Sensitive information like API keys and database passwords are stored in a `.env` file. Be sure to add `.env` to `.gitignore` to keep these details private.

# Technologies Used

- **Python**: Used for scripting and data processing
- **Twitter API via RapidAPI**: Extracts tweets for analysis
- **TextBlob**: Sentiment analysis of tweets
- **PostgreSQL**: Stores cleaned data
- **Apache Airflow**: Orchestrates and schedules the data pipeline
- **Docker**: Provides a consistent environment for development and execution

# Running Locally

To run the project locally without Docker, make sure you have Python and PostgreSQL installed. You can use a Python virtual environment and run each script sequentially. Update the database connection details accordingly.

# Future Improvements

- **Automated Coin Detection**: Implement more sophisticated techniques for automatic detection of new meme coins.
- **Data Visualization**: Build a dashboard to display the sentiment and trends visually, using tools like Power BI or Tableau.
- **Enhanced Analysis**: Utilize natural language processing (NLP) for more advanced sentiment and trend analysis.

# Contributing

Contributions are welcome! Please create an issue or submit a pull request for any features or bug fixes you would like to see.

# License

This project is licensed under the MIT License.

# Contact

For questions or suggestions, feel free to reach out to me via [GitHub](https://github.com/xsechaba).

# Summary

This project is a great way to explore the world of cryptocurrency trends, data analysis, and workflow orchestration using modern data engineering tools. Feel free to contribute or fork the repository to make it even better!
