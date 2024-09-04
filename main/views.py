from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306212083',
        'name': 'Muhammad Yahya Ayyas',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
