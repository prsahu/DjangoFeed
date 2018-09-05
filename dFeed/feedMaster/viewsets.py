from rest_framework import viewsets
from rest_framework import permissions 
from feedreader.models import Entry
from .serializers import ArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    # for q in queryset:
    #     print(q.title)
    #     print(q.link)
    serializer_class = ArticleSerializer
    permission_classes = (permissions.AllowAny,)
    def get_feed(self, entry_id):
        self.user = Entry.objects.get(id=entry_id)
        return self.user