from django.shortcuts import render
from django.http import HttpResponse
from django import forms
import io
from django.http import FileResponse
import pandas as pd


df = pd.DataFrame({'Наименование работ': ['СТРОИТЕЛЬНЫЕ РАБОТЫ',
                                              'Грунтовка стен',
                                              'Шпатлевка и шлифовка стен под покрас',
                                              'Оклейка стен путинкой',
                                              'Грунтовка стен перед покраской',
                                              'Покраска стен безвоздушкой',
                                              'Шпатлевка стен под обои',
                                              'шпатлевка откосов и стен менее 60см (путинка,шитрок,покрас)',
                                              'Поклейка обоев',
                                              'Монтаж гкл фрамуг на дверной проем',
                                              'Перегородки 600 мм',
                                              'ПОЛЫ',
                                              'Грунтовка пола',
                                              'Установка плинтусов',
                                              'Устновка теневого профиля',
                                              'Плитка напольная крупноформатная',
                                              'Укладка ламината',
                                              'ЭЛЕКТРОМОНТАЖНЫЕ РАБОТЫ',
                                              'Установка точечных светильников',
                                              'Установка подвесов',
                                              'Установка светодиодной ленты',
                                              'Установка подрозетников',
                                              'Установка выключателей розеток',
                                              'Установка бра',
                                              'ПРОЧИЕ',
                                              'Монтаж мансардной лестницы',
                                              'Установка фартука',
                                              'Ванна под ключ',
                                              'Гостевой сан узел',''],
                       'Стоимость': [0, 100, 800, 150, 70, 300, 300, 800, 350, 500, 2000, 0,
                                     50, 600, 800, 2500, 400, 0, 500, 1000, 300, 200, 200, 1000,
                                     0, 5000, 32000, 250000, 140000,0],
                       'Обьем': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
                       'Ед.Из.': ['', 'кв.м', 'кв.м', 'кв.м', 'кв.м', 'кв.м', 'кв.м', 'пм', 'кв.м', 'шт', 'шт',
                                  '', 'кв.м', 'п.м', 'пм', 'кв.м', 'кв.м', '', 'шт', 'шт', 'пм', 'шт', 'шт', 'шт',
                                  '', 'шт', 'шт', 'шт', 'шт','ИТОГО:'],
                       'Итого':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0]})


ss_data = []
ee_data = []
pp_data = []
oo_data = []




def main(request):
    data = {
        'stritems': [
            ["Грунтовка стен", "кв.м"],
            ["Шпатлевка и шлифовка стен под покрас", "кв.м"],
            ["Оклейка стен паутинкой", "кв.м"],
            ["Грунтовка стен перед покраской", "кв.м"],
            ["Покраска стен безвоздушкой", "кв.м"],
            ["Шпатлевка стен под обои", "кв.м"],
            ["Поклейка обоев", "кв.м"],
            ["Шпатлевка откосов и стен менее 60 см (паутинка, шитрок, покрас)", "пм"],
            ["Монтаж гкл фрамуг на дверной проем", "шт"],
            ["Перегородки 600 мм","шт"]
        ],
    }
    return render(request, "main.html", context=data)
def electr(request):
    data = {
        'stritems': [
            ["Установка подрозетников", "шт"],
            ["Установка точечных светильников", "шт"],
            ["Установка подвесов", "шт"],
            ["Установка светодиодной ленты", "шт"],
            ["Установка выключателей розеток", "шт"],
            ["Установка бра", "шт"]
        ]
    }
    return render(request, "electr.html", context=data)
def pol(request):
    data = {
        'stritems': [
            ["Грунтовка пола", "кв.м"],
            ["Установка плинтусов (полиуретановые)", "пм"],
            ["Установка теневого профиля", "пм"],
            ["Плитка напольная крупноформатная", "кв.м"],
            ["Укладка ламината", "кв.м"]
        ]
    }
    return render(request, "pol.html", context=data)
def others(request):
    data = {
        'stritems': [
            ["Монтаж монсардной лестницы (по необходимости)", "шт"],
            ["Устройство фартука", "шт"],
            ["Ванная под ключ", "шт"],
            ["Гостевой сан узел", "шт"],

        ]
    }
    return render(request, "other.html", context=data)


def s_data(request,a,b,c,d,e,f,g,h,i,j):
    global ss_data
    ss_data = [a,b,c,d,e,f,g,h,i,j]
    #df['Обьем'] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1000,0,0,0,0,0,0,0,0,0,0,0,2,2,2]
    #df.to_excel('data.xlsx')
    print(ss_data)
    return render(request, "stroika.html")
def e_data(request,a,b,c,d,e,f):
    global ee_data
    ee_data = [a, b, c, d, e, f]
    print(ee_data)
    return render(request, "electr.html")
def p_data(request,a,b,c,d,e):
    global pp_data
    pp_data = [a, b, c, d, e]
    print(pp_data)
    return render(request, "pol.html")
def o_data(request,a,b,c,d):
    global oo_data
    oo_data = [a, b, c, d]
    print(oo_data)
    return render(request, "other.html")
def save(request):
    global  ss_data
    global ee_data
    global pp_data
    global oo_data
    global df
    if len(ss_data)==0:ss_data = [0,0,0,0,0,0,0,0,0,0]
    if len(ee_data) == 0: ee_data = [0, 0, 0, 0, 0, 0]
    if len(pp_data) == 0: pp_data = [0, 0, 0, 0, 0]
    if len(oo_data) == 0: oo_data = [0, 0, 0, 0]
    data = [0]+ss_data+[0]+pp_data+[0]+ee_data+[0]+oo_data+[0]
    price = df['Стоимость']
    itogo = []
    for i in range(len(data)):
        itogo.append(data[i]*price[i])
    print(data)
    print(len(data))
    print('ХУЙ')
    df['Обьем'] = data
    itogo[-1] = sum(itogo)
    df['Итого'] = itogo
    df.to_excel('data.xlsx',index=False)
    return FileResponse(open('data.xlsx','rb'))