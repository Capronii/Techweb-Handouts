from django.shortcuts import render, redirect
from .models import Note

# Comando pra rodar o postgres
# docker run --rm --name pg-docker -e POSTGRES_PASSWORD=escolhaumasenha -d -p 5432:5432 -v C:\Users\egdag\docker\volumes\postgres:\var\lib\postgresql\data postgres

def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        newNote = Note(title = title, content = content)
        newNote.save()
        return redirect('index')
    else:
        allNotes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': allNotes})

def update_note(request, id):
    if request.method == 'POST':
        id = request.POST.get('id')
        title = request.POST.get('title')
        content = request.POST.get('content')
        updatedNote = Note(id = id, title = title, content = content)
        updatedNote.save()
        return redirect('index')
    
    else:
        allNotes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': allNotes})  

def delete_note(request, id):
    if request.method == 'POST':
        note = Note.objects.get(id = id)
        note.delete()
        return redirect('index')
    
    else:
        allNotes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': allNotes})