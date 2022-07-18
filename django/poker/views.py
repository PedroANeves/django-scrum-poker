from django.shortcuts import render

def index(request):
    return render(request, 'poker/index.html')

def table(request, table_name):
    return render(request, 'poker/table.html', {'table_name': table_name})
