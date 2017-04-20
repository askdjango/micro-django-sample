import os
from importlib import import_module
settings = import_module(os.environ.get('DJANGO_SETTINGS_MODULE', 'settings.dev'))
from django import forms
from django.conf.urls.static import static
from django.db import models
from django.shortcuts import redirect, render
from django_micro import configure, get_app_label, route, run, urlpatterns

configure(settings.__dict__)

from django.conf import settings


#
# models
#

class Post(models.Model):
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = get_app_label()
        ordering = ['-id']


#
# forms
#

class MultiplePhotoForm(forms.Form):
    image_file_list = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


#
# views/urls
#

@route(r'^$', name='index')
def index(request):
    post_list = Post.objects.all()
    return render(request, 'index.html', {'post_list': post_list})


@route(r'^(?P<pk>\d+)/$', name='detail')
def detail(request, pk):
    return render(request, 'detail.html')


@route(r'^new/$', name='new')
def new(request):
    if request.method == 'POST':
        form = MultiplePhotoForm(request.POST, request.FILES)
        if form.is_valid():
            for image_file in request.FILES.getlist('image_file_list'):
                post = Post()
                post.image.save(image_file.name, image_file)
                post.save()
            return redirect('index')
    else:
        form = MultiplePhotoForm()
    return render(request, 'form.html', {'form': form})


media_patterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns.extend(media_patterns)


#
# run
#

application = run()

