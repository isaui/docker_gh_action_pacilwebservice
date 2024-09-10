from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2206028932',
        'name': 'Upi (Luthfi)',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
