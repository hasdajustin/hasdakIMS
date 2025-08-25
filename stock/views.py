from django.shortcuts import render

# Create your views here.
def stock_view(request):
    return render(request, 'pages/stock.html')