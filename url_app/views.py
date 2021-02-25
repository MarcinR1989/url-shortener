import string
import random
from django.shortcuts import render, redirect
from django.views import View

from .forms import UrlForm
from .models import ShortUrl


class ShortURLView(View):
    def get(self, request):
        form = UrlForm()
        return render(request, 'short_url.html', {'form': form})

    def post(self, request):
        form = UrlForm(request.POST)
        if form.is_valid():
            slug_data = ShortUrl.objects.all()
            for n in range(10):
                slug = ''.join(random.choice(string.ascii_letters)
                               for x in range(10))
                if not slug_data.filter(slug=slug):
                    break
            url = form.cleaned_data['url']
            new_url = ShortUrl(url=url, slug=slug)
            new_url.save()
            context = {'new_url': new_url,
                       'hidden': 'hidden',
                       'domain': request.build_absolute_uri(), }
            return render(request, 'short_url.html', context)


class UrlRedirectView(View):
    def get(self, request, slugs):
        data = ShortUrl.objects.get(slug=slugs)
        return redirect(data.url)


