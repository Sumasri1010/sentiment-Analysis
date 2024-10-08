import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
# Download NLTK data (if not already downloaded)
nltk.download('vader_lexicon')
def analyze_sentiment(text):
    # Initialize the sentiment intensity analyzer
    sia = SentimentIntensityAnalyzer()

    # Get sentiment scores
    sentiment_scores = sia.polarity_scores(text)

    # Determine sentiment based on the compound score
    if sentiment_scores['compound'] >= 0.05:
        return 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# Example text
text = "I love working with Python! It's such a powerful language."
# text = "I am so stressed with Java as it is very difficult! It's such a difficult language."
# Perform sentiment analysis
result = analyze_sentiment(text)
# Display the result
print(f"Sentiment: {result}")
