import pandas as pd
import nltk
import requests
import matplotlib.pyplot as plt

nltk.download('stopwords')
nltk.download('punkt')

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from PIL import Image
from io import BytesIO


# Function to recommend by content based
def recommend(df, title):

    # Matching the genre with the dataset and reset the index
    data = df
    data.reset_index(level=0, inplace=True)

    # Convert the index into series
    indices = pd.Series(data.index, index=data['title'])
    

    # Converting the book description into vectors and used bigram
    tf = TfidfVectorizer(analyzer='word', ngram_range=(2, 2), min_df=1, stop_words='english')
    tfidf_matrix = tf.fit_transform(data['cleaned_desc'])

    # Calculating the similarity measures based on Cosine Similarity
    sg = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # Get the index corresponding to original_title
    try:
        idx = indices[title]
    except:
        column_names = ['title', 'image', 'subjects']
        empty_df = pd.DataFrame(columns = column_names)
        print("error, empty df")
        return empty_df

    # Get the pairwsie similarity scores
    sig = list(enumerate(sg[idx]))

    # Sort the books
    sig = sorted(sig, key=lambda x: x[1], reverse=True)

    # Scores of the 5 most similar books
    sig = sig[1:6]

    # Book indicies
    movie_indices = [i[0] for i in sig]

    # Top 5 book recommendation
    rec = pd.DataFrame(data[['title', 'image', 'subjects']].iloc[movie_indices])

    # It reads the top 5 recommend book url and print the images
    # for i in rec['image']:
    #     response = requests.get(i)
    #     img = Image.open(BytesIO(response.content))
    #     plt.figure()
    #     print(plt.imshow(img))

    return rec