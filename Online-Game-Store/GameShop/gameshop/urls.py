from django.conf.urls import url, include

from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^shop$', views.shop, name='shop'),
    url(r'^play/(?P<game_id>[0-9]+)/$', views.play, name='play'),
    url(r'^payment$', views.payment, name='payment'),
    url(r'^developer$', views.developer, name='developer'),
    url(r'^add$', views.add_game, name='add'),
    url(r'^modify/(?P<game_id>[0-9]+)/$', views.modify_game, name='modify'),
    url(r'^remove/(?P<game_id>[0-9]+)/$', views.remove_game, name='remove'),
    url(r'^search$', views.search, name='search'),
    url(r'^verify$', views.verify_email, name='verify'),
    url(r'^statistics/(?P<game_id>[0-9]+)/$', views.game_statistics, name='statistics'),
]

