from django.shortcuts import render
from displayData.scripts.time_provider import get_time
from displayData.scripts.read_data import get_data


# Create your views here.
def welcome(request):
    context = {'time': get_time()}
    return render(request, 'displayData/welcome.html', context)
    # return HttpResponse("Welcome to Data Display Home Page")


def table_view(request):
    data_file_name = "restaurant.csv"
    context = {'time': get_time(), 'd': get_data(data_file_name)}
    return render(request, 'displayData/table_data.html', context)


def table_view_two(request):
    data_file_name = "boston.csv"
    context = {'time': get_time(), 'd': get_data(data_file_name)}
    return render(request, 'displayData/table_data_two.html', context)
