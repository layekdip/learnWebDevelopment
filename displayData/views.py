import json
import os
import pandas as pd
# from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


# Create your views here.
def welcome(request):
    today = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    temp = "Welcome to Dashboard"
    temp = temp + " , " + "Current Date time : {}".format(today)
    context = {'d': temp}
    return render(request, 'displayData/welcome.html', context)
    # return HttpResponse("Welcome to Data Display Home Page")


def table_view(request):
    env_dict = {'PROJECT_HOME_DIR': "D:\\Learning\\PythonLearning\\learnWebDevelopment\\displayData"}
    data_file_name = "restaurant.csv"
    input_data = os.path.join(env_dict['PROJECT_HOME_DIR'], 'data_source', data_file_name)
    print(input_data)
    df = pd.read_csv(input_data)
    # table_data = df.to_html()
    # return HttpResponse(table_data)
    # parsing the DataFrame in json format.
    json_records = df.reset_index().to_json(orient='records')
    data = json.loads(json_records)
    context = {'d': data}
    return render(request, 'displayData/table_data.html', context)


def table_view_two(request):
    env_dict = {'PROJECT_HOME_DIR': "D:\\Learning\\PythonLearning\\learnWebDevelopment\\displayData"}
    data_file_name = "boston.csv"
    input_data = os.path.join(env_dict['PROJECT_HOME_DIR'], 'data_source', data_file_name)
    print(input_data)
    df = pd.read_csv(input_data)
    # table_data = df.to_html()
    # return HttpResponse(table_data)
    # parsing the DataFrame in json format.
    json_records = df.reset_index().to_json(orient='records')
    data = json.loads(json_records)
    context = {'d': data}
    return render(request, 'displayData/table_data_two.html', context)
