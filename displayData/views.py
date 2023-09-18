from django.shortcuts import render
from displayData.forms import DataSourceNameForm
from displayData.scripts.time_provider import get_time
from displayData.scripts.read_data import get_data
from displayData.scripts.plot_data import plot_data_with_bar
from django.views.decorators.csrf import csrf_exempt


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


def data_analysis(request):
    data_file_name = "restaurant.csv"
    x_axis = 'city'
    y_axis = 'tip'
    context = {'time': get_time(),
               'graph': plot_data_with_bar(data_file_name, x_axis, y_axis),
               'data_source': 'Data file in use : {}'.format(data_file_name),
               'graph_param': 'Fields in use for graph - X Axis : {} , Y Axis : {}'
               .format(x_axis, y_axis)}
    return render(request, 'displayData/data_analysis.html', context)


@csrf_exempt
def interactive_data_analysis(request):
    if request.method == "POST":
        data_file_name = request.POST.get('interactive_data_analysis', None)
        x_axis = request.POST.get('x_axis_val', None)
        y_axis = request.POST.get('y_axis_val', None)
        context = {'time': get_time(),
                   "data_file": data_file_name,
                   "x_axis": x_axis,
                   "y_axis": y_axis,
                   'graph': plot_data_with_bar(data_file_name, x_axis, y_axis)
                   }
        return render(request, 'displayData/interactive_data_analysis.html', context)
    else:
        context = {'time': get_time()}
        return render(request, 'displayData/interactive_data_analysis.html', context)
