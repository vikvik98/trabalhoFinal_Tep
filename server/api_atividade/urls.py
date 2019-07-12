from django.contrib import admin
from django.urls import path
from filmes import views
from rest_framework_jwt.views import (obtain_jwt_token,
                                      refresh_jwt_token)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/login/', obtain_jwt_token),
    path('auth/refresh-token/', refresh_jwt_token),
    path('filmes/', views.FilmeList.as_view(), name= views.FilmeList.name),
    path('filmes/<int:id>', views.FilmeDetail.as_view(), name= views.FilmeDetail.name),
    path('categorias/<int:id>', views.CategoriaDetail.as_view(), name= views.CategoriaDetail.name),
    path('categorias/', views.CategoriaList.as_view(), name= views.CategoriaList.name),
    path('', views.ApiRoot.as_view(), name= views.ApiRoot.name),
    path('usuarios/', views.UserList.as_view(), name=views.UserList.name),
    path('usuarios/<int:id>/', views.UserDetail.as_view(), name=views.UserDetail.name)
]
