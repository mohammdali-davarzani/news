from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from django.db.models import Q
from elasticsearch_dsl import Q as EQ
from elasticsearch_dsl import Search
from elasticsearch import Elasticsearch
from itertools import chain
import urllib.parse as change_url

from .models import NewsContents
from .documents import NewsDocument
from .serializers import NewsSerializer
from .pagination import StandardResultsSetPagination, SmallResultsSetPagination, LargeResultsSetPagination

# Create your views here.

client = Elasticsearch()
s = Search(using=client, index='news_contents')

class NewsList(ListAPIView):
    queryset = NewsContents.objects.filter(
            Q(is_duplicate=False) &
            Q(is_disable=False)
        ).order_by("-id")
    serializer_class = NewsSerializer
    pagination_class = SmallResultsSetPagination


    def filter_queryset(self, queryset):
        search_lookups = list()
        filter_lookups = {}
        is_search_lookups = False
        is_filter_lookups = False


        for name, value in NewsContents.searching_lookups:
            param = self.request.GET.get(value)
            if param:
                search_lookups.append(param)
                is_search_lookups = True

        for name, value in NewsContents.filtering_lookups:
            param = self.request.GET.get(value)
            if param:
                filter_lookups[name] = param
                is_filter_lookups = True


        if is_search_lookups == True and is_filter_lookups == True:
            phrase = search_lookups[0]

            search_query = s.query(
                EQ("match", news_title=phrase) | EQ("match", news_source=phrase) |
                EQ("match", news_lead=phrase) | EQ("match", news_content=phrase)
            )

            filter_query = queryset.filter(**filter_lookups)

            queryset_output = list(
                        chain(search_query, filter_query)
                    )

            return queryset_output[::-1]

        elif is_search_lookups == True and is_filter_lookups == False:
            phrase = search_lookups[0]

            search_query = s.query(
                EQ("match", news_title=phrase) | EQ("match", news_source=phrase) |
                EQ("match", news_lead=phrase) | EQ("match", news_content=phrase)
            )

            queryset_output = search_query

            return queryset_output[::-1]

        elif is_search_lookups == False and is_filter_lookups == True:

            filter_query = queryset.filter(**filter_lookups)

            queryset_output = filter_query

            return queryset_output[::-1]


        else :

            queryset_output = queryset.filter(
                    Q(is_duplicate=False) &
                    Q(is_disable=False)
                ).order_by("-id")

            return queryset_output
