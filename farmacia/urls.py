from django.conf.urls import url
from farmacia import views

urlpatterns = [
    url(r'getPazienti', views.get_pazienti, name='get_pazienti'),
    url(r'getMedici', views.get_medici, name='get_medici'),
    url(r'getCase', views.get_case, name='get_case'),
    url(r'getProdotti', views.get_prodotti, name='get_prodotti'),
    url(r'home', views.index, name='index'),
    url(r'getFarmaci', views.get_farmaci, name='get_farmaci'),
    url(r'getVendite', views.get_vendite, name='get_vendite'),
    url(r'getBrevettati', views.get_brevettati, name='get_brevettati'),
    url(r'getGenerici', views.get_generici, name='get_generici'),
    url(r'getProfumeria', views.get_profumeria, name='get_profumeria'),
    url(r'getCosmetici', views.get_cosmetici, name='get_cosmetici'),
    url(r'getIgiene', views.get_igiene, name='get_igiene'),
    url(r'getCuraBimbo', views.get_cura_bimbo, name='get_cura_bimbo'),
    url(r'getPrescrizioni', views.get_prescrizioni, name='get_prescrizioni'),
    #url(r'prova',views.prova, name='prova'),
    url(r'insPaziente', views.insert_paziente, name='insert_paziente'),
    url(r'insMedico', views.insert_medico, name='insert_medico'),
    url(r'insCasa', views.insert_casa, name='insert_casa'),
    url(r'insBrevettato', views.insert_brevettato, name='insert_brevettato'),

]
