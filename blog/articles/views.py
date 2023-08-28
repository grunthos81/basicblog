from django.shortcuts import render
from .models import *
from django.views import View

#single article view
class ArticleView(View):
    def get(self, request, pagename):
        article = Article.objects.get(permalink='/'+pagename)
        return render(request, 'articles/article.html', {'article' : article})

#section view
class SectionView(View):
    def get(self, request, section):
        chosen_section = Section.objects.get(section_name=section)
        if section == 'home':
            articles = Article.objects.all()
        else:
            articles = Article.objects.filter(section = chosen_section, draft = False)
        latest_article = articles[0]
        second_article = articles[1]
        other_articles = articles[2:]
        content = {'latest' : latest_article,
                   'second' : second_article,
                   'other' : other_articles,
                   'section' : chosen_section}
        return render(request, 'articles/section.html', content)




