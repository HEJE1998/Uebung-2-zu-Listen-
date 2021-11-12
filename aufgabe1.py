#Jeldrik Hemme#
#ETS 2021
#12.11.2021

#Hardware: wird nicht benötigt 

#Version:0.2

#Aufgabe: Schreiben Sie ein Programm, das mithilfe einer for-Schleife alle durch 9 teilbaren Zahlen zwischen zwei zuvor eingegebenen Grenzen
#in eine Liste schreibt und dann ausgibt.

#Eingabe der Werte 
unteregrenze = input('untere Grenze eingeben ')
oberegrenze = input('obere grenze eingeben ')

zahlenliste = []

for zahlen in range (int(unteregrenze),int(oberegrenze)):
    if zahlen % 9 == 0:
        zahlenliste.append(zahlen)

for liste in zahlenliste:
    print(liste)

    
