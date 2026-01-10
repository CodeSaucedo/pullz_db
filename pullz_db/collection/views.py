from django.shortcuts import render
from .models import Comic
from .forms import ComicForm
from django.shortcuts import redirect

# Create your views here.

def home(request):
    comics = Comic.objects.order_by('-created_at')[:10]

    if request.method == 'POST':
        form = ComicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ComicForm()

    


    return render(request, 'collection/home.html', {'comics': comics, 'form': form})

def pull_list(request):
    pulls = Comic.objects.filter(status='wanted').order_by('title')
    return render(request, 'collection/pull_list.html', {'pulls': pulls})

def directory(request):
    comics = Comic.objects.all()

    publisher = request.GET.get('publisher')
    status = request.GET.get('status')

    if publisher:
        comics = comics.filter(publisher__iexact=publisher)
    if status:
        comics = comics.filter(status=status)
    
    comics = comics.order_by('title', 'issue_number')
    
    return render(request, 'collection/directory.html', {'comics': comics})
