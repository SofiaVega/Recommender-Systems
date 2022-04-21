#el algoritmo de max
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
import re
from pandas.api.types import is_numeric_dtype

import requests
import plotly.express as px
import sklearn
from sklearn.decomposition import TruncatedSVD

import sklearn
from sklearn.decomposition import TruncatedSVD
import warnings


import os

def path_to_image_html(path):
    return '<img src="'+ path + '" width="60" >'

def df_recommend(recommend, user_rating):
    recommend=recommend[:5]
    year=[]
    author = []
    image_url=[]
    for i in recommend:
        for j in user_rating.index:
            if user_rating['bookTitle'][j]==i:
                year.append(user_rating['yearOfPublication'][j])
                author.append(user_rating['bookAuthor'][j])
                image_url.append(user_rating['imageUrlM'][j])  
                break
    recommend_df=pd.DataFrame([recommend, year, author ,image_url]).T
    #rec = pd.DataFrame(data[['title', 'image', 'subjects']].iloc[movie_indices])
    recommend_df.columns=['Recommend Books','Year of Publication','Author','Image']
    
    image_cols = ['Image']


    format_dict = {}
    for image_col in image_cols:
        format_dict[image_col] = path_to_image_html
    
    return recommend_df


def recommend_book(df_pivot, corr_mat, name, user_rating):
    #name=input("Enter the Name of the Book : ")
    book_names = df_pivot.columns
    print(book_names)
    book_list = list(book_names)
    try:
        if name in book_list:
            print("in book list")
            book_index = book_list.index(name) 
            corr_book = corr_mat[book_index] 
            print("Recommendation for " + name + " are:")
            recommend=list(book_names[(corr_book<1.0) & (corr_book>0.8)][1:])
            return df_recommend(recommend, user_rating)

        else:
            name=" "+name
            book_index = book_list.index(name) 
            corr_book = corr_mat[book_index] 
            print("Recommendation for " + name + " are:")
            recommend=list(book_names[(corr_book<1.0) & (corr_book>0.8)][1:])
            return df_recommend(recommend, user_rating)
    except:
        # return empty df of form ['Recommend Books','Year of Publication','Author','Image']
        column_names = ['Recommend Books','Year of Publication','Author','Image']
        empty_df = pd.DataFrame(columns = column_names)
        print("error, empty df")
        return empty_df
        print("Enter the Book Name Again")
        #recommend_book(df_pivot,corr_mat, name)

def recommend2(book_name):
    data_path = os.path.abspath("Book_Recommender_System_App/static/tables/out.csv")
    df = pd.read_csv(data_path)
    data_path_rating = os.path.abspath("Book_Recommender_System_App/static/tables/rating.csv")
    df_rating = pd.read_csv(data_path_rating)
    X = df.values.T
    SVD = TruncatedSVD(n_components=12, random_state=17)
    matrix = SVD.fit_transform(X)
    warnings.filterwarnings("ignore",category =RuntimeWarning)
    corr = np.corrcoef(matrix)
    return recommend_book(df, corr, book_name, df_rating)

    booksjson = {
        "books":[
            {
                "isbn":"9781593279509",
                "title":"Eloquent JavaScript, Third Edition",
                "subtitle":"A Modern Introduction to Programming",
                "author":"Marijn Haverbeke",
                "published":"2018-12-04T00:00:00.000Z",
                "publisher":"No Starch Press",
                "pages":472,
                "description":"JavaScript lies at the heart of almost every modern web application, from social apps like Twitter to browser-based game frameworks like Phaser and Babylon. Though simple for beginners to pick up and play with, JavaScript is a flexible, complex language that you can use to build full-scale applications.",
                "website":"http://eloquentjavascript.net/"
            }
        ]
    }
    df = pd.read_json(booksjson)
    return df