from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import (
    EmptyPage, PageNotAnInteger, Paginator)
from .models import *
from rest_framework import generics, viewsets
from . import serializers
from django.http import JsonResponse

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

class FindMatches(View):

    def get(self, request, *args, **kwargs):
        transactions = []
        uid = kwargs.get('uid')
        #uid = '1'
        me = User.objects.get(id=uid)
        #me = User.objects.get(username='anthony')
        goods = Good.objects.filter(user=me)
        # Get everything I need.
        for i_need in Need.objects.filter(user=me):
            # Get everything I can give.
            for i_give in goods:
                # See who needs what I can give.
                for user2 in User.objects.all():
                    # Do they have what I need?
                    for user2_good in Good.objects.filter(user=user2):
                        if i_need.name == user2_good.name:
                            #transaction = Transaction.objects.create()
                            #tug1 = TransactionUserGroup.objects.create(transaction=transaction, user=uid, good=i_give, need=i_need)
                            #tug2 = TransactionUserGroup.objects.create(transaction=transaction, user=user2, good=i_need, need=i_give)
                            transactions.append([
                                {'giver': me.username, 'good': str(i_give.name), 'need': str(i_need.name)},
                                {'giver': user2.username, 'good': str(i_need.name), 'need': str(i_give.name)}
                            ])
                        else:
                            # No they don't.
                            # See if anyone needs what user2 has.
                            for user3_need in Need.objects.filter(name=user2_good.name):
                                # Does user3 have something I want?
                                user3 = user3_need.user
                                for user3_good in Good.objects.filter(user=user3):
                                    if i_need == user3_good:
                                        # Three way trade found.
                                        transactions.append([
                                            {'giver': me.username, 'good': str(i_give.name), 'need': str(i_need.name)},
                                            {'giver': user2.username, 'good': str(i_need.name), 'need': str(i_give.name)},
                                            {'giver': user3.username, 'good': str(user3_good.name), 'need': str(user3_need.name)}
                                        ])
        return JsonResponse(transactions, safe=False)
