from django.shortcuts import render
import os
import pandas as pd
import json
from .template_tags.synopsis_algorithm import recommend

from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import re


# Create your views here.
def index(request):
    if request.GET.get('mybtn'):

        data_path = os.path.abspath("Book_Recommender_System_App/static/tables/data.csv")
        df = pd.read_csv(data_path)

        # Function for removing NonAscii characters
        def _removeNonAscii(s):
            return "".join(i for i in s if ord(i) < 128)

        # Function for converting into lower case
        def make_lower_case(text):
            return text.lower()

        # Function for removing stop words
        def remove_stop_words(text):
            text = text.split()
            stops = set(stopwords.words("english"))
            text = [w for w in text if not w in stops]
            text = " ".join(text)
            return text

        # Function for removing punctuation
        def remove_punctuation(text):
            tokenizer = RegexpTokenizer(r'\w+')
            text = tokenizer.tokenize(text)
            text = " ".join(text)
            return text

        # Function for removing the html tags
        def remove_html(text):
            html_pattern = re.compile('<.*?>')
            return html_pattern.sub(r'', text)

        # Applying all the functions in description and storing as a cleaned_desc
        # df['cleaned_desc'] = df['synopsis'].apply(_removeNonAscii)a
        df['cleaned_desc'] = df.synopsys.apply(func=make_lower_case)
        df['cleaned_desc'] = df.cleaned_desc.apply(func=remove_stop_words)
        df['cleaned_desc'] = df.cleaned_desc.apply(func=remove_punctuation)
        df['cleaned_desc'] = df.cleaned_desc.apply(func=remove_html)

        print(request.GET.get('mytextbox'))
        print(list(recommend(df, title=request.GET.get('mytextbox'))["image"]))

        context = {"Recommendation": list(recommend(df, title=request.GET.get('mytextbox'))["image"])}
        return render(request, 'pages/index.html', context)

    return render(request, 'pages/index.html')


def cf(request):
    return render(request, 'pages/cf.html')


def about(request):
    return render(request, 'pages/about.html')


def charts(request):
    return render(request, 'pages/charts.html')


def tables(request):

    data_path = os.path.abspath("Book_Recommender_System_App/static/tables/goodreads_library_export.csv")
    df = pd.read_csv(data_path)
    df = df.drop(labels=["Author l-f",
                         "Additional Authors",
                         "ISBN",
                         "ISBN13",
                         "Date Read",
                         "Bookshelves",
                         "Bookshelves with positions",
                         "My Review",
                         "Spoiler",
                         "Private Notes",
                         "Read Count",
                         "Recommended For",
                         "Recommended By",
                         "Owned Copies",
                         "Original Purchase Date",
                         "Original Purchase Location",
                         "Condition",
                         "Condition Description",
                         "BCID"
                         ], axis=1)

    df_json = json.dumps(df.values.tolist())
    # parsing the DataFrame in json format.
    json_records = df.reset_index().to_json(orient='records')
    data = []
    data = json.loads(json_records)
    context = {"data": data}

    return render(request, 'pages/tables.html', context)


def request_page(request):

  if request.GET.get('mybtn'):
      print("1")
      data = pd.read_csv("static/tables/data.csv")
      print(request.GET.get('mytextbox'))
      return render(request, 'pages/index.html', recommend(data, title=request.GET.get('mytextbox')))

