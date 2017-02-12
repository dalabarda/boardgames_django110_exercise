"""boardgames URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views # to create login, logout, sign up and Password reset




#from main import views
from main import views as main_views


# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^$', include('main.urls')),

# ]



urlpatterns = [
	url(r'^admin/', admin.site.urls),
    url(r'^user/', include('user.urls')),
    url(r'^tictactoe/', include('tictactoe.urls')),
	url(r'^$', main_views.home, name='boardgames_home'),
    url(r'^login/$', auth_views.login, name='boardgames_login'),
	url(r'^logout/$', auth_views.logout, {'next_page': 'boardgames_home'} ,name='boardgames_logout'),
]



# # # this works also!
# urlpatterns += [ 
#     url(r'^login/$', 
#         auth_views.login,
#         name='boardgames_login'),

#     url(r'^logout$', 
#         auth_views.logout,
#         {'next_page': 'boardgames_home'},
#         name='boardgames_logout'),

# ]

# this is the old version in django 1.6
# # 
# urlpatterns += [
# 	'django.contrib.auth.views',
 
# 	url(r'^login/$', 'login',
# 		{'template_name': 'login.html'},
# 		name='boardgames_login'),

# 	url(r'^logout/$', 'logout',
# 		{'next_page': 'boardgames_home'},
# 		name='boardgames_logout'),

# ]


### this may work also
# url(
#     regex=r'^login/$', 
#     view=login, 
#     kwargs={'template_name': 'login.html'}, 
#     name='login'
# ),
# url(
#     regex=r'^logout/$', 
#     view=logout, 
#     kwargs={'next_page': '/'}, 
#     name='logout'
# ),