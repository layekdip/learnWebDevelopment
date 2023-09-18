from django.urls import path
from . import views

app_name = "displayData"
urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("table_view/", views.table_view, name="table_view"),
    path("table_view_two/", views.table_view_two, name="table_view_two"),
    path("data_analysis/", views.data_analysis, name="data_analysis"),
    path("interactive_data_analysis/", views.interactive_data_analysis, name="interactive_data_analysis"),
]
