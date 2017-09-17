from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import (
    EmptyPage, PageNotAnInteger, Paginator)
from .models import *
from rest_framework import generics, viewsets

from . import serializers

# from django_filters.rest_framework import DjangoFilterBackend

#PostSerializer:
class GoodViewSet(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = serializers.GoodSerializer
    # filter_fields = ('',)

# class UserInfoViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = serializers.UserInfoSerializer
class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = serializers.UserInfoSerializer
    filter_fields = ('',)

class CanonicalGoodViewSet(viewsets.ModelViewSet):
    queryset = CanonicalGood.objects.all()
    serializer_class = serializers.CanonicalGoodSerializer
    # filter_fields = ('',)

class NeedViewSet(viewsets.ModelViewSet):
    queryset = Need.objects.all()
    serializer_class = serializers.NeedSerializer
    # filter_fields = ('',)

class GoodList(View):
    page_arg = 'page'
    paginate_by = 50
    template_name = 'trade/good_list.html'

    def get(self, request, page_number=1):
        good_list = Good.objects.all()
        paginator = Paginator(good_list, self.paginate_by)
        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator(
                paginator.num_pages)
        if page.has_previous():
            prev_url = reverse('good_list',
                args=[page.previous_page_number()])
        else:
            prev_url = None
        if page.has_next():
            next_url = reverse('good_list',
                args=[page.next_page_number()])
        else:
            next_url = None
        context = {
            'is_paginated': page.has_other_pages(),
            'paginator': paginator,
            'prev_url': prev_url,
            'next_url': next_url,
            'tag_list': page}
        return render(request, self.template_name, context)
