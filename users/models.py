from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)

class TechArticle(Article):
    tech_field = models.CharField(max_length=100)

class NewsArticle(Article):
    news_source = models.CharField(max_length=100)

def create_article(article_type, data):
    if article_type == 'tech':
        return TechArticle.objects.create(**data)
    elif article_type == 'news':
        return NewsArticle.objects.create(**data)
    else:
        return Article.objects.create(**data)

class VideoContent(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='videos/')
    duration = models.DurationField()

class AudioContent(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='audio/')
    duration = models.DurationField()

class ImageContent(models.Model):
    title = models.CharField(max_length=200)
    file = models.ImageField(upload_to='images/')

class ContentFactory:
    def create_content(self, content_type, data):
        if content_type == 'video':
            return VideoContent.objects.create(**data)
        elif content_type == 'audio':
            return AudioContent.objects.create(**data)
        elif content_type == 'image':
            return ImageContent.objects.create(**data)
        else:
            raise ValueError('Unknown content type')

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_moderated = models.BooleanField(default=False)


class Tag(models.Model):
    name = models.CharField(max_length=50)

class Category(models.Model):
    name = models.CharField(max_length=50)
    articles = models.ManyToManyField(Article)

