
from django.conf.urls import url
from .views import (
            ProductListView,
            #product_list_view,
            ProductDetailSlugView, 
            #ProductDetailView, 
            #product_detail_view,
            #ProductFeaturedListView,
            #ProductFeaturedDetailView
            )

urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),
]

