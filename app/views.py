from django.shortcuts import redirect, render
from .forms import PhotoForm
from .models import Photo


def photo_list(request):
    photos = Photo.objects.order_by('created_at')
    return render(request, 'app/photo_list.html', {'photos': photos})

def photo_upload(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('photo_list')
    else:
        form = PhotoForm()
    return render(request, template_name='app/photo_upload.html', context={'form': form})