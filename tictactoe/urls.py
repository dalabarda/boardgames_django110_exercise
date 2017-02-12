from django.conf.urls import include, url

from tictactoe import views as tictactoe_views
from .views import AllGamesList


urlpatterns = [
	url(r'^invite$', tictactoe_views.new_invitation, name='tictactoe_invite'),
	url(r'^invitation/(?P<pk>\d+)/$', tictactoe_views.accept_invitation, name='tictactoe_accept_invitation'),
	url(r'^game/(?P<pk>\d+)/$', tictactoe_views.game_detail, name='tictactoe_game_detail'),
	url(r'^game/(?P<pk>\d+)/do_move$', tictactoe_views.game_do_move, name='tictactoe_game_do_move'),
	url(r'^game/all', AllGamesList.as_view()),
]


