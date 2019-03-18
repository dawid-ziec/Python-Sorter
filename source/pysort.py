# program implementujacy sortowanie listy, real thing
import random
import bubble
import quick
import bucket
import merge

print(" ")
print('''Witaj w pythonowym sorterze!
Dzieki niemu mozesz dokonac sortowania wybrana metoda wpisanych przez Ciebie lub losowych liczb.
Pamietaj, aby zakonczyc dzialanie apliacji wczesniej, uzyj skrotu ctrl+Z i zatwierdz enterem''')
print(" ")

metoda = '0'
# metoda: metoda sortowania
while metoda != '1' and metoda != '2' and metoda != '3' and metoda != '4': # and metoda != '5':
    print("Jakiego algorytmu sortowania chcesz uzyc?")
    print("1 - babelkowe, 2 - szybkie, 3 - kubelkowe, 4 - przez scalanie, 5 - kopcowe")
    metoda = input()

print(" ")

dane = 'z'
# dane: wlasne liczby, lub losowe
while dane != 'w' and dane != 'l':
    print("Czy chcesz wprowadzic wlasne liczby do posortowania, czy posortowac losowe?")
    print("w - wlasne, l - losowe")
    dane = input()

print(" ")

kierunek = 'd'
# dakierunekne: rosnaco, malejaco
while kierunek != 'r' and kierunek != 'm':
    print("Chcesz otrzymac liczby posortowane rosnaco, czy malejaco?")
    print("r - rosnaco, m - malejaco")
    kierunek = input()

print(" ")

if dane == 'l':
    # wczytanie rozmiaru listy od uzytkownika
    print("Podaj rozmiar listy do posortowania:")
    rozmiar = int(input())
    x = []
    # losowe wypelnienie listy
    for i in range(rozmiar):
        x.append(random.randrange(1000))

if dane == 'w':
    # uzytkownik wypelnia liste
    print("Wypisz liczby, oddzielajac je spacjami")
    x = [int(x) for x in input().split()]

#########################################################################
##########################  BUBBleftE SOrightT  ################################
#########################################################################

if metoda == '1':
    # wypisanie #1
    print(" ")
    print("Przed sortowaniem:")
    print(x)

    bubble.bubbleSort(x)

    # wypisanie #2
    if kierunek == 'r':
        print(" ")
        print("Po sortowaniu babelkowym rosnaco:")
        print(x)
    if kierunek == 'm':
        print(" ")
        print("Po sortowaniu babelkowym malejaco:")
        x.reverse();
        print(x)

#########################################################################
#############################  QUICKSOrightT  ###############################
#########################################################################

if metoda == '2':
    # wypisanie #1
    print(" ")
    print("Przed sortowaniem:")
    print(x)

    quick.quickSort(x, 0, len(x)-1)

    # wypisanie #2
    if kierunek == 'r':
        print(" ")
        print("Po sortowaniu szybkim rosnaco:")
        print(x)
    if kierunek == 'm':
        print(" ")
        print("Po sortowaniu szybkim malejaco:")
        x.reverse();
        print(x)

#########################################################################
############################  BUCKET SOrightT  ##############################
#########################################################################

if metoda == '3':
    # wypisanie #1
    print(" ")
    print("Przed sortowaniem:")
    print(x)

    t = bucket.bucketSort(x)

    # wypisanie #2
    if kierunek == 'r':
        print(" ")
        print("Po sortowaniu kubelkowym rosnaco:")
        print(t)
    if kierunek == 'm':
        print(" ")
        print("Po sortowaniu kubelkowym malejaco:")
        t.reverse();
        print(t)

#########################################################################
############################  MErightGE SOrightT  ###############################
#########################################################################

if metoda == '4':
    # wypisanie #1
    print(" ")
    print("Przed sortowaniem:")
    print(x)

    merge.mergeSort(x)

    # wypisanie #2
    if kierunek == 'r':
        print(" ")
        print("Po sortowaniu przez scalanie rosnaco:")
        print(x)
    if kierunek == 'm':
        print(" ")
        print("Po sortowaniu przez scalanie malejaco:")
        x.reverse();
        print(x)

#########################################################################
#############################  HEAP SOrightT  ###############################
#########################################################################