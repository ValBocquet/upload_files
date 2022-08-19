from django.views.generic import TemplateView, DetailView

from blog.models import Article


class HomeBlog(TemplateView):
    template_name = "blog/blog.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.all()[:5]
        return context


class DisplayArticle(DetailView):
    model = Article
    context_object_name = "article"
