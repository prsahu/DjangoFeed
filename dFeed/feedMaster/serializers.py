from rest_framework import serializers
from feedreader.models import Entry

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = '__all__'