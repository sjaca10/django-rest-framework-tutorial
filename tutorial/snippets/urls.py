from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from snippets.views import SnippetViewSet, UserViewSet, api_root
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

# Binding ViewSets to URLs explicitly
# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })

# Using Routers
# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# urlpatterns = format_suffix_patterns([
urlpatterns = [
    # For the second example
    # url(r'^snippets/$', views.snippet_list),
    # url(r'^snippets/(?P<pk>[0-9]+)$', views.snippet_detail),


    # For example class based views
    # url(r'^$', views.api_root),

    # url(r'^snippets/$', views.SnippetList.as_view(), name='snippet-list'),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(),
    #     name='snippet-detail'),
    # url(r'^snippets/(?P<pk>[0-9]+)/highlight/$',
    #     views.SnippetHighlight.as_view(), name='snippet-highlight'),

    # url(r'^users/$', views.UserList.as_view(), name='user-list'),
    # url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(),
    #     name='user-detail'),

    # Binding ViewSets to URLs explicitly
    # url(r'^snippet/$', snippet_list, name='snippet-list'),
    # url(r'^snippet/(?P<pk>[0-9]+)/$', snippet_detail, name='snippet-detail'),
    # url(r'^snippet/(?P<pk>[0-9]+)/highlight$', snippet_highlight,
    #     name='snippet-highlight'),

    # url(r'^users/$', user_list, name='user-list'),
    # url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls'))

]

# urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth', include('rest_framework.urls'))
]
