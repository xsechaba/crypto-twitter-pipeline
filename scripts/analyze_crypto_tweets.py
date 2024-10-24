import pandas as pd
from collections import Counter

def analyze_hashtags():
    df = pd.read_csv('cleaned_crypto_tweets.csv')
    
    # Extract hashtags from the 'text' column
    df['hashtags'] = df['text'].str.findall(r"#(\w+)")
    
    # Flatten and count hashtags
    all_hashtags = df['hashtags'].explode()
    hashtag_counts = Counter(all_hashtags.dropna())
    
    # Convert to DataFrame
    hashtag_df = pd.DataFrame(hashtag_counts.items(), columns=['Hashtag', 'Count'])
    hashtag_df = hashtag_df.sort_values(by='Count', ascending=False).reset_index(drop=True)
    
    # Save hashtag analysis to CSV
    hashtag_df.to_csv('hashtag_frequency.csv', index=False)
    print("Hashtag frequency analysis saved to hashtag_frequency.csv")
    
    return hashtag_df

if __name__ == "__main__":
    analyze_hashtags()
