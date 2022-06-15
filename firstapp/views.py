from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UserForm
from .forms import SecretForm
import pandas as pd
from firstapp.forms import UserForm
from firstapp.models import Person

                                                                                                                                                      
#                        ..................................................................'.'''''.......                               
#                      ......''''''''',''''''''''''''''''''''''''''''''''''''''''''''''''',,,,,,,,,'......                              
#                    .......'',,,',,,,,'''''''''''''''''''''''''''''''''''''''''''''''',,,,,,;;;;;,,''......                            
#                   ........',,,,,,,,,,,,,,,,,,,,,,,,,,'''''''''''',,,'''''''''''''',,,,,,,,;;::;;,,''........                          
#                  .........',,,;;,,,,;,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,''''''',,,,,,,;;;:::;;,,,'.......                          
#                 ..........,;;;;;;;;;;;;,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,;;;;:::;;;,,,,'''.....                         
#               ...........',;;;;;;:::;;;;,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,;;:::::;;;,;;,'''......                        
#              ............,;;;;;:::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,,,,,,,,,,,,,,,,,,,,;;;;::::;;;;;;;,'''.......                       
#                ..........,;;;::cc::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,,,,,,,,,,,,,,;;:::::;;;;;;;;;,'''........                      
#                ....... ..,;;:ccc::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,,,,,,,,,,,;;;::::;;;;;;;::;,''''........                     
#                 ...    .';:cccc:;;;;;;;;;::::;::;;;;;;;;;;;;;;;;;;;;;;;;;;;;,,,,,,;;;;::::::;;;;:::;'''''........                     
#         ..         .....,:ccc::;;;;,,,,;;::::::::::;;;;;;::::::::;;;;;;;;;;;;;;;;;;;;::::::;;::::::,''''..........                    
#        ....       .....':::::;;;;;;,,,,;;;::::::::::::::::::::::::::::;;;;;;;;;;;;;;:::::::;;:::::;'...'...........                   
#       ......      ....';:;;;;;;;,,;,,,,,;;;::::::::::::::::::::::cccccc::::;;;;;;;::::cc::::::::c:,...............                    
#      .........  ......,;;;;;;;;,,,''..',,;;;::::::::;;;;;;;;;;;::::ccccccc:::::::::::ccc:::::::c:,...............                     
#     ..................,;,,,,,''.......',,;,'';::::::;;;;;;;;;;;;:::::ccccccc:::ccccccccc:::::::c;..................                   
#     ...........................   ...',,,;;'..',;::;;;;;;;;;;;;:;;::::::ccccccccccccccc:::;:::c;.....................                 
#    ............... ..         .....',,;;;,;;,....',,,;;;;;;;;;;;;;;;;;;:::cccccclccccc::::::cc;'.....................                 
#   ....................    ....''',,,;;;;;;;;;;,'.................'',,,;;;::cccllllccc::;;;:::;.......................                 
#   .....................  ..,,,,,,,,,;;;;;;;;,;;;,'...        .. ......',;;::clllllcc::;;;:::,.........................                
#   .........................',,,,,,,,,,;;;;;;;,,,,;,,'.....        ......',;:clllllc::;;;;:;'...........................               
#   ...........................',,,,,,,,,,,,;;;;,,,;;;,,,,''.......    ....';:cclllcc;;,;;;'.............................               
#   ..............................,,,''''',,,;;;,,,,,,,,,,,,,,,,,,''...  ...,;cclllc;;,;,'...  ...........................              
#   ............................ ..........',,;;,,,,,,,,,,,,,,,,,,,,,,''.....;clllc:;,....    ...........................               
#   .......................        .;c,.    .,;;,','''''''''''''',,,,,,,,''..,cllc;;'. ..   .............................               
#    ....................         .;ol;.  ...';,,,''''..... ......'',,,,,,,'';cll::,..,,'. ..............................               
#     .................           .cd:.   .. ';,,,''....''.       ..'',,,,,,,:llc;'.'''..  .............................                
#      ............              ..,::...   .,;,,,'...,cl;.  ..     ..'',,',;clc,'''...     ............................                
#        ........                .;,''......';;,,,'...:oc.  .''.  .. .',,,,;clc,..'..        ...........................                
#                                ':;''....',::;,,,'...:l:.   ..   ';..,::ccloc,'''.             .......................                 
#                                .::;;,,;;:::;,,'''...,:c,..... ..;;',:looool:'...              .....................                   
#                   ....         .;:;;:::cc:;,'''''.....,,'......',',clooooo:.                    ..................                    
#                     ............,;,;::c::;,''',,'''...........',,;clloool,.                        ..............                     
#                         .........;;:ccc;,,''',,,,,,,'''''''''',;;:cccll:'.                           ..  ..                           
#                           ..    .;:cc::;,,,,,,,,,,,,,,,,,,,,,,,,;;;::::'.....                                                         
#                           ......,:ccc::;::::;;;,,,,,,,,,,,,,,',,,,;;::,. ......      ...                                              
#                           .....,:ccc::cccclcc::;;;,,,,,,','''',,,,;::;;,........... ..;'                                              
#                           ....':cccccllooooolcc:::;''',,''''',,,;;:c,..;''......... ..,.                                              
#                            ...;cllcloodddddollccc;,''''',,,,,,,;;cc,. ............. ...                                               
#                            ..;cllooodddxddoolcc:;,'''''',,,,,;;:cc;.      ................                                            
#                           .':clloodddddddolc:;;;,,''''',,,,;;::cc;.          ...............                                          
#                            .;::clooddoollc::::c:::;,'''',,;:::cc;.                   ..........                                       
#                            ..,,;:ccccc::::cllooollc:;,'',;:::cc,.                       ........                                      
#                            ....'',;,,,',;::ccccclllc:;'',;:ccc,.                            ....                                      
#                                 .','.....',;::::;;:cc;,,;:cc:'.                                                                       
#                                 .',......'',,;:c::;;;,,,;:;,'.  .                                                                     
#                                 ....    .......'',,,'..','......                                                                      


def GetQwerySetTOListElementsBySTR(str1):
    stritems = Person.objects.values()
    liststritems = []
    for elem in stritems:
        str = elem['str']
        if str == str1:
            liststritems.append([elem['name'], elem['type']])
    return liststritems

def GetQwerySetTOCart(str1):
    stritems = Person.objects.values()
    liststritems = []
    itogprice = 0
    for elem in stritems:
        str = elem['str']
        if str in str1 and elem['value'] != 0:
            resprice = elem['ratio']*elem['value']
            itogprice += resprice
            liststritems.append([elem['name'], elem['value'], elem['type'], resprice])
    return liststritems, itogprice

def SetValuesToSQLElements(str1, mas):
    stritems = Person.objects.values()
    i = 0
    for elem in stritems:
        str = elem['str']
        if str == str1:
            item = Person.objects.get(id=elem['id'])
            item.value += mas[i]
            item.save(update_fields=["value"])
            i += 1


def ResetValuesSQLElements(str1):
    stritems = Person.objects.values()
    i = 0
    for elem in stritems:
        str = elem['str']
        if str == str1:
            item = Person.objects.get(id=elem['id'])
            item.value = 0
            item.save(update_fields=["value"])
            i += 1

def CartResetValuesSQLElements():
    stritems = Person.objects.values()
    i = 0
    for elem in stritems:
        item = Person.objects.get(id=elem['id'])
        item.value = 0
        item.save(update_fields=["value"])
        i += 1

def SaveAsExelTable():
    stritems = Person.objects.values()
    df = {
        'Название': [],
        'Количество': [],
        'Цена': []
    }
    itogprice = 0
    for elem in stritems:
        value = elem['value']
        if value != 0:
            price = value * elem['ratio']
            itogprice += price
            df['Название'].append(elem['name'])
            df['Количество'].append(value)
            df['Цена'].append(price)
    df['Название'].append('Итог')
    df['Количество'].append(' ')
    df['Цена'].append(itogprice)
    pd.DataFrame(df).to_excel('./output.xlsx')

def main(request):
    str = 1
    
    # form
    userform = UserForm()
    scrform = SecretForm()
    if request.method == 'POST':
        if 'addnewelem' in request.POST:
            name = request.POST.get("name")
            type = request.POST.get("type")
            ratio = request.POST.get("ratio")
            item = Person(name=name, type=type, str=str, value=0, ratio=ratio)
            item.save()
        elif 'savevals' in request.POST:
            mas = list(map(int, request.POST.get("mas").split()))
            SetValuesToSQLElements(str, mas)
        elif 'resetvals' in request.POST:
            ResetValuesSQLElements(str)
    data = {
        'stritems': GetQwerySetTOListElementsBySTR(str),
        'form': userform,
        'sform': scrform
    }
    return render(request, "main.html", context=data)

def electr(request):
    str = 2
    
    # form
    userform = UserForm()
    scrform = SecretForm()
    if request.method == 'POST':
        if 'addnewelem' in request.POST:
            name = request.POST.get("name")
            type = request.POST.get("type")
            ratio = request.POST.get("ratio")
            item = Person(name=name, type=type, str=str, value=0, ratio=ratio)
            item.save()
        elif 'savevals' in request.POST:
            mas = list(map(int, request.POST.get("mas").split()))
            SetValuesToSQLElements(str, mas)
        elif 'resetvals' in request.POST:
            ResetValuesSQLElements(str)
    data = {
        'stritems': GetQwerySetTOListElementsBySTR(str),
        'form': userform,
        'sform': scrform
    }
    return render(request, "electr.html", context=data)
def pol(request):
    str = 3
    
    # form
    userform = UserForm()
    scrform = SecretForm()
    if request.method == 'POST':
        if 'addnewelem' in request.POST:
            name = request.POST.get("name")
            type = request.POST.get("type")
            ratio = request.POST.get("ratio")
            item = Person(name=name, type=type, str=str, value=0, ratio=ratio)
            item.save()
        elif 'savevals' in request.POST:
            mas = list(map(int, request.POST.get("mas").split()))
            SetValuesToSQLElements(str, mas)
        elif 'resetvals' in request.POST:
            ResetValuesSQLElements(str)
    data = {
        'stritems': GetQwerySetTOListElementsBySTR(str),
        'form': userform,
        'sform': scrform
    }
    return render(request, "pol.html", context=data)
def others(request):
    str = 4
    
    # form
    userform = UserForm()
    scrform = SecretForm()
    if request.method == 'POST':
        if 'addnewelem' in request.POST:
            name = request.POST.get("name")
            type = request.POST.get("type")
            ratio = request.POST.get("ratio")
            item = Person(name=name, type=type, str=str, value=0, ratio=ratio)
            item.save()
        elif 'savevals' in request.POST:
            mas = list(map(int, request.POST.get("mas").split()))
            SetValuesToSQLElements(str, mas)
        elif 'resetvals' in request.POST:
            ResetValuesSQLElements(str)
    data = {
        'stritems': GetQwerySetTOListElementsBySTR(str),
        'form': userform,
        'sform': scrform
    }
    return render(request, "other.html", context=data)



def cart(request):
    reslist, itogprice = GetQwerySetTOCart([1,2,3,4])
    print(itogprice)
    scrform = SecretForm()
    data = {
        'stritems': reslist,
        'sform': scrform,
        'itogprice': itogprice
    }
    
    if request.method == 'POST':
        if 'resetcartvals' in request.POST:
            CartResetValuesSQLElements()
            return HttpResponseRedirect("/")
        elif 'xmlsave' in request.POST:
            print('hi')
            SaveAsExelTable()
            
    
    return render(request, 'cart.html', context=data)
