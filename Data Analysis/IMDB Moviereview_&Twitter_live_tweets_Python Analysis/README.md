# Large Movie Review Dataset

The Large Movie Review Dataset is a corpus of 50,000 movie reviews from IMDB that have been classified as either positive or negative. More information about the dataset can be found at https://ai.stanford.edu/~amaas/data/sentiment/.

In this project, we are going to define a tokenizer to calculate sentiment scores based on the words used in the movie reviews, so that we can analyze whether the reviews are positive or negative.

## Code Explanation

### Downloading IMDB Corpus

The code starts by downloading the IMDB movie review dataset from a URL (https://storage.googleapis.com/wd13/IMDBReviewSent.txt) and storing it in a list called `imdb_corpus`. The dataset contains 50,000 movie reviews, each with a label indicating whether it's positive or negative.

### Tokenization

Next, a tokenizer function `tokenize(doc)` is defined, which takes a document as input and tokenizes it into a list of tokens. The tokenizer uses regular expressions to match emoticons, words, and ellipses in the document. The tokens are then converted to lowercase. The tokenizer function will be used later to tokenize the movie reviews in the `imdb_corpus`.

### Lexicon Creation

After the tokenization step, the code creates a lexicon, which is a dictionary that will store sentiment scores for each token in the corpus. The code calculates the sentiment scores by counting the occurrences of each token in positive and negative movie reviews, and then applying a formula that takes into account the ratio of positive to negative occurrences. The sentiment scores are stored in the `lexicon` dictionary.

### Score Message Function

A scoring function `score_message(doc)` is defined, which takes a document as input and calculates the sentiment score for that document using the lexicon created in the previous step. The function iterates over the tokens in the document, and if a token is found in the lexicon, its sentiment score is added to a running total. The function returns the total sentiment score for the document.

# Live Twitter Data Dataset

The code then moves on to analyzing live Twitter data related to Netflix and Disney+. First, a Twitter API bearer token is uploaded from a file. Then, a function `get_tweets(query, bearer_token, number_of_tweets)` is defined, which takes a search query, bearer token, and the number of tweets to return as input, and uses the Twitter API to fetch recent tweets related to the query. The fetched tweets are stored in a list called `tweets`.

### Saving and Loading Tweet Data

The fetched tweets are then saved to a local JSON file called `tweets.json` using the `json` module. The code includes functions to upload and load files in Google Colab, which are used to save and load the JSON file.

### Analyzing Twitter Data

The code continues with analyzing the fetched tweets. First, the lexicon created earlier is installed in Google Colab using the `uploaded_files` function. Then, the sentiment scores of the tweets are calculated using the `score_message()` function, which takes each tweet as input and returns its sentiment score. The sentiment scores are used to generate summary statistics for the tweets, such as the average sentiment score, the number of positive and negative tweets, and the most positive and negative tweets.
