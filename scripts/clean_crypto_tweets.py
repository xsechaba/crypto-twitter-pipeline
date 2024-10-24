import pandas as pd
from textblob import TextBlob
import re
import html

# Function to clean special characters and decode text
def clean_text(text):
    text = html.unescape(text)
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    return text

def clean_and_analyze_tweets():
    # Read raw data
    df = pd.read_csv('raw_crypto_tweets.csv')
    
    # Clean and analyze the data
    df['text'] = df['text'].apply(clean_text)
    df['sentiment'] = df['text'].apply(lambda text: TextBlob(text).sentiment.polarity)
    
    # Save cleaned data
    df.to_csv('cleaned_crypto_tweets.csv', index=False)
    print("Cleaned data saved to cleaned_crypto_tweets.csv")
    return df

if __name__ == "__main__":
    clean_and_analyze_tweets()

