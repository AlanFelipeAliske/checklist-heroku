
from core import views
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='login/')),
    path('admin/', admin.site.urls),
    path('usuario/', views.usuario, name='usuario'),

    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
    path('index/', views.index, name='index'),
    path('inicio/', views.inicio, name='inicio'),
    
    path('checklist/', views.checklist, name='checklist'),
    path('checklist/detalhes/', views.detalhes, name='detalhes'),

    path('veiculos/', views.veiculos, name='veiculo'),
    path('veiculos/editar/', views.editar_veiculo, name='editar'),
    path('veiculos/editar/submit', views.submit_veiculo, name='submit_veiculo'),
    path('veiculos/excluir/<int:id>/', views.excluir_veiculo, name='excluir_veiculo'),
    path('veiculos/adicionar/', views.adicionar_veiculo, name='adicionar'),
    path('veiculos/adicionar/submit', views.submit_adicionar_veiculo, name='submit_adicionar'),

    path('equipamentos/', views.equipamento, name='equipamento'),
    path('equipamentos/editar/', views.editar_equipamento, name='editar_equipamento'),
    path('equipamentos/editar/submit', views.submit_equipamento, name='submit_equipamento'),
    path('equipamentos/excluir/<int:id>/', views.excluir_equipamento, name='excluir_equipamento'),
    path('equipamentos/adicionar/', views.adicionar_equipamento, name='adicionar'),
    path('equipamentos/adicionar/submit', views.submit_adicionar_equipamento, name='submit_equipamento'),

]
