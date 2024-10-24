import requests
import pandas as pd
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Get the RapidAPI key from environment variables
rapidapi_key = os.getenv('RAPIDAPI_KEY')

# RapidAPI credentials
url = "https://twitter-api45.p.rapidapi.com/search.php"
querystring = {
    "query": "100x OR moonshot OR meme coin OR doge OR shiba OR floki OR pepecoin OR pump OR bullish OR HODL OR altcoin", 
    "search_type": "Top"
}
headers = {
    "x-rapidapi-key": rapidapi_key,
    "x-rapidapi-host": "twitter-api45.p.rapidapi.com"
}

def extract_crypto_tweets():
    response = requests.get(url, headers=headers, params=querystring)
    
    if response.status_code == 200:
        data = response.json()
        tweet_list = []
        for tweet in data['timeline']:
            tweet_list.append({
                'user': tweet['screen_name'],
                'text': tweet['text'],
                'favorite_count': tweet['favorites'],
                'retweet_count': tweet['retweets'],
                'created_at': tweet['created_at'],
            })
        df = pd.DataFrame(tweet_list)
        
        # Save the raw data to CSV
        df.to_csv('raw_crypto_tweets.csv', index=False)
        print("Raw data saved to raw_crypto_tweets.csv")
        return df
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

if __name__ == "__main__":
    extract_crypto_tweets()
