from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from django.db.models import Q

from .models import NewsContents
from .serializers import NewsSerializer
from .pagination import StandardResultsSetPagination, SmallResultsSetPagination, LargeResultsSetPagination

# Create your views here.


class NewsList(ListAPIView):
    queryset = NewsContents.objects.filter(
                    Q(is_disable=False) & Q(is_duplicate=False)
                ).order_by('-news_date_time')
    serializer_class = NewsSerializer
    pagination_class = SmallResultsSetPagination
