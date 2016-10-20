# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
from django.conf.urls import url

from demo.views import HomeView, NotUseId, UseId, NotUseIdSmall, UseIdSmall, NotUseSelectRelated, UseSelectRelated, \
    NotUseSelectRelatedBetterCycle, NotUsePrefetchRelated, UsePrefetchRelated, NotUseBulkCreate, UseBulkCreate

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^not-use-id-small/$', NotUseIdSmall.as_view(), name='not_use_id_small'),
    url(r'^use-id-small/$', UseIdSmall.as_view(), name='use_id_small'),
    url(r'^not-use-id/$', NotUseId.as_view(), name='not_use_id'),
    url(r'^use-id/$', UseId.as_view(), name='use_id'),

    url(r'^not-use-sr/$', NotUseSelectRelated.as_view(), name='not_use_sr'),
    url(r'^not-use-sr-opt/$', NotUseSelectRelatedBetterCycle.as_view(), name='not_use_sr_opt'),
    url(r'^use-sr/$', UseSelectRelated.as_view(), name='use_sr'),

    url(r'^not-use-pr/$', NotUsePrefetchRelated.as_view(), name='not_use_pr'),
    url(r'^use-pr/$', UsePrefetchRelated.as_view(), name='use_pr'),

    url(r'^not-use-bc/$', NotUseBulkCreate.as_view(), name='not_use_bc'),
    url(r'^use-bc/$', UseBulkCreate.as_view(), name='use_bc'),
]
