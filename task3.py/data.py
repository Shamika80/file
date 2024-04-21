positive_words = ["amazing", "wonderful", "enjoyed", "breathtaking", "beautiful", "memorable", "fantastic", "unforgettable", "excellent", "enlightening", "unique", "stunning", "delicious", "mesmerizing"]
negative_words = ["disappointing", "poor", "lackluster", "scarce", "overcrowded", "bad"]

def analyze_sentiment(text):
  
  positive_count = 0
  negative_count = 0
  words = text.lower().split()  
  for word in words:
    if word in positive_words:
      positive_count += 1
    elif word in negative_words:
      negative_count += 1
  return positive_count, negative_count

def main():
  """Reads travel blog entries, analyzes sentiment, and prints a summary."""
  try:
    with open("travel_blogs.txt", 'r') as file:
      text = file.read()
  except FileNotFoundError:
    print("Error: File not found: travel_blogs.txt")
    return

  # Extract individual blog entries (assuming each entry starts on a new line)
  blog_entries = text.strip().splitlines()

  # Analyze sentiment for each entry and accumulate counts
  total_positive = 0
  total_negative = 0
  for entry in blog_entries:
    positive_count, negative_count = analyze_sentiment(entry)
    total_positive += positive_count
    total_negative += negative_count

  # Print sentiment analysis summary
  print("Sentiment Analysis Summary:")
  print(f"Total Positive Words: {total_positive}")
  print(f"Total Negative Words: {total_negative}")

if __name__ == "__main__":
  main()