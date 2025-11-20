from django.shortcuts import render,redirect
from .forms import NoteForm
from .models import Note

# Create your views here.
def index(request):
    if request.method=='POST':
        form=NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form=NoteForm()
        return render(request,'index.html',{'form':form})
    
def success(request):
    notes=Note.objects.all().order_by('-updated_at')
    return render(request,'success.html',{'notes':notes})

