from rest_framework import serializers
from .models import Article, TechArticle, NewsArticle

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class TechArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechArticle
        fields = '__all__'

class NewsArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsArticle
        fields = '__all__'



class VideoContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoContent
        fields = '__all__'

class AudioContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioContent
        fields = '__all__'

class ImageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageContent
        fields = '__all__'
