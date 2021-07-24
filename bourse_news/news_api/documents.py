from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

from .models import NewsContents


@registry.register_document
class NewsDocument(Document):

    class Index:
        name = 'news_contents'
        settings = {
            'number_of_shards':1,
            'number_of_replicas':0
        }

    class Django:
        model = NewsContents
        fields = (
            'news_source', 'news_url', 'news_date_time', 'news_title',
            'news_image', 'news_lead', 'news_content', 'is_duplicate',
            'is_disable',
        )
