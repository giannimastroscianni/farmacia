# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import models
import traceback


def index(request):
    context_dict = {'string': "Benvenuto!"}
    return render(request, 'farmacia/index.html', context=context_dict)


def get_pazienti(request):
    try:
        dao = models.Dao()
        pazienti = dao.get_pazienti()
        context_dict = {'pazienti': pazienti}
    except:
        traceback.print_exc()
    return render(request, 'farmacia/pazienti.html', context=context_dict)


def get_medici(request):
    try:
        dao = models.Dao()
        medici = dao.get_medici()
        context_dict = {'medici': medici}
    except:
        traceback.print_exc()
    return render(request, 'farmacia/medici.html', context=context_dict)


def get_case(request):
    try:
        dao = models.Dao()
        case = dao.get_case()
        context_dict = {'case': case}
    except:
        traceback.print_exc()
    return render(request, 'farmacia/case.html', context=context_dict)


def get_prodotti(request):
    try:
        dao = models.Dao()
        prodotti = dao.get_prodotti()
        context_dict = {'prodotti': prodotti}
    except:
        traceback.print_exc()
    return render(request, 'farmacia/prodotti.html', context=context_dict)


def get_farmaci(request):
    try:
        dao = models.Dao()
        farmaci = dao.get_farmaci()
        context_dict = {'farmaci': farmaci}
    except:
        traceback.print_exc()
    return render(request, 'farmacia/farmaci.html', context=context_dict)


def get_brevettati(request):
    try:
        dao = models.Dao()
        brevettati = dao.get_brevettati()
        context_dict = {'brevettati': brevettati}
    except:
        traceback.print_exc()
    return render(request, 'farmacia/brevettati.html', context=context_dict)


def get_generici(request):
    try:
        dao = models.Dao()
        generici = dao.get_generici()
        context_dict = {'generici': generici}
    except:
        traceback.print_exc()
    return render(request, 'farmacia/generici.html', context=context_dict)


def get_profumeria(request):
    try:
        dao = models.Dao()
        profumeria = dao.get_profumeria()
        context_dict = {'profumeria': profumeria}
    except:
        traceback.print_exc()
    return render(request, 'farmacia/di_profumeria.html', context=context_dict)


def get_cosmetici(request):
    try:
        dao = models.Dao()
        cosmetici = dao.get_cosmetici()
        context_dict = {'cosmetici': cosmetici}
    except:
        traceback.print_exc()
    return render(request, 'farmacia/cosmetici.html', context=context_dict)


def get_igiene(request):
    try:
        dao = models.Dao()
        igiene = dao.get_igiene()
        context_dict = {'igiene': igiene}
    except:
        traceback.print_exc()
    return render(request, 'farmacia/igiene.html', context=context_dict)


def get_cura_bimbo(request):
    try:
        dao = models.Dao()
        cura_bimbo = dao.get_cura_bimbo()
        context_dict = {'cura_bimbo': cura_bimbo}
    except:
        traceback.print_exc()
    return render(request, 'farmacia/cura_bimbo.html', context=context_dict)


def get_vendite(request):
    try:
        dao = models.Dao()
        vendite = dao.get_vendite()
        context_dict = {'vendite': vendite}
    except:
        traceback.print_exc()
    return render(request, 'farmacia/vendite.html', context=context_dict)


def get_prescrizioni(request):
    try:
        dao = models.Dao()
        prescrizioni = dao.get_prescrizioni()
        context_dict = {'prescrizioni': prescrizioni}
    except:
        traceback.print_exc()
    return render(request, 'farmacia/prescrizioni.html', context=context_dict)


def insert_paziente(request):
    try:
        dao = models.Dao()
        if request.method == "POST":
            cf = request.POST.get('cf')
            dao.insert_paziente(cf)
    except:
        traceback.print_exc()
    return render(request, 'farmacia/inspaz.html')


def insert_medico(request):
    try:
        dao = models.Dao()
        if request.method == "POST":
            cod = request.POST.get('cod')
            dao.insert_medico(cod)
    except:
        traceback.print_exc()
    return render(request, 'farmacia/insmed.html')


def insert_casa(request):
    try:
        dao = models.Dao()
        if request.method == "POST":
            nome = request.POST.get('nome')
            recapito = request.POST.get('recapito')
            dao.insert_casa(nome, recapito)
    except:
        traceback.print_exc()
    return render(request, 'farmacia/inscasa.html')


def insert_brevettato(request):
    try:
        dao = models.Dao()
        case = dao.get_case()
        dic = {'case': case}
        if request.method == "POST":
            id = request.POST.get('id')
            nome = request.POST.get('nome')
            descrizione = request.POST.get('descrizione')
            casa = request.POST.get('casa')
            pos = casa.index(',')
            nome_casa = casa[1:pos]
            recapito_casa = casa[pos + 1:-1]
            prescrivibile = request.POST.get('prescrivibile')
            durata = request.POST.get('durata')
            dao.insert_brevettato(id, nome, descrizione, nome_casa, recapito_casa, prescrivibile, durata)
    except:
        traceback.print_exc()
    return render(request, 'farmacia/insbrev.html', context=dic)


def insert_generico(request):
    try:
        dao = models.Dao()
        case = dao.get_case()
        brevettati = dao.get_brevettati()
        dic = {'case': case, 'brevettati': brevettati}
        if request.method == "POST":
            id = request.POST.get('id')
            nome = request.POST.get('nome')
            descrizione = request.POST.get('descrizione')
            casa = request.POST.get('casa')
            pos = casa.index(',')
            nome_casa = casa[1:pos]
            recapito_casa = casa[pos + 1:-1]
            prescrivibile = request.POST.get('prescrivibile')
            brevettato = request.POST.get('brevettato')
            dao.insert_generico(id, nome, descrizione, nome_casa, recapito_casa, prescrivibile, brevettato)
    except:
        traceback.print_exc()
    return render(request, 'farmacia/insgen.html', context=dic)


def insert_cosmetico(request):
    try:
        dao = models.Dao()
        case = dao.get_case()
        dic = {'case': case}
        if request.method == "POST":
            id = request.POST.get('id')
            nome = request.POST.get('nome')
            descrizione = request.POST.get('descrizione')
            casa = request.POST.get('casa')
            pos = casa.index(',')
            nome_casa = casa[1:pos]
            recapito_casa = casa[pos + 1:-1]
            dao.insert_cosmetico(id, nome, descrizione, nome_casa, recapito_casa)
    except:
        traceback.print_exc()
    return render(request, 'farmacia/inscosm.html', context=dic)


def insert_igiene(request):
    try:
        dao = models.Dao()
        case = dao.get_case()
        dic = {'case': case}
        if request.method == "POST":
            id = request.POST.get('id')
            nome = request.POST.get('nome')
            descrizione = request.POST.get('descrizione')
            casa = request.POST.get('casa')
            pos = casa.index(',')
            nome_casa = casa[1:pos]
            recapito_casa = casa[pos + 1:-1]
            dao.insert_igiene(id, nome, descrizione, nome_casa, recapito_casa)
    except:
        traceback.print_exc()
    return render(request, 'farmacia/insig.html', context=dic)


def insert_cura_bimbo(request):
    try:
        dao = models.Dao()
        case = dao.get_case()
        dic = {'case': case}
        if request.method == "POST":
            id = request.POST.get('id')
            nome = request.POST.get('nome')
            descrizione = request.POST.get('descrizione')
            casa = request.POST.get('casa')
            pos = casa.index(',')
            nome_casa = casa[1:pos]
            recapito_casa = casa[pos + 1:-1]
            dao.insert_cura_bimbo(id, nome, descrizione, nome_casa, recapito_casa)
    except:
        traceback.print_exc()
    return render(request, 'farmacia/inscurbim.html', context=dic)


def insert_vendita(request):
    try:
        dao = models.Dao()
        if request.method == "POST":
            id = request.POST.get('id')
            data = request.POST.get('data')
            acquisti = request.POST.get('acquisti')
            dao.insert_vendita(id, data, acquisti)
    except:
        traceback.print_exc()
    return render(request, 'farmacia/insven.html')


def insert_prescrizione(request):
    try:
        dao = models.Dao()
        pazienti = dao.get_pazienti()
        medici = dao.get_medici()
        vendite = dao.get_distinct_vendite()
        dic = {'pazienti': pazienti, 'medici': medici, 'vendite': vendite}
        if request.method == "POST":
            id = request.POST.get('id')
            paziente = request.POST.get('paziente')
            medico = request.POST.get('medico')
            vendita = request.POST.get('vendita')
            farmaci = request.POST.get('farmaci')
            dao.insert_prescrizione(id, paziente, medico, vendita, farmaci)
    except:
        traceback.print_exc()
    return render(request, 'farmacia/inspre.html', context=dic)


def prova(request):
    try:
        dao = models.Dao()
        prodotti = dao.get_prodotti()
        dic = {'prodotti': prodotti}
        if request.method == "POST":
            id = request.POST.get('id')
            data = request.POST.get('data')
            acquisti = request.POST.get('acquisti')
            print id, data, acquisti
    except:
        traceback.print_exc()
    return render(request, 'farmacia/test.html', context=dic)
