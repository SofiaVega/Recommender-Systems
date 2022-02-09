from django.shortcuts import render
import os
import pandas as pd
import json


# Create your views here.
def index(request):
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
