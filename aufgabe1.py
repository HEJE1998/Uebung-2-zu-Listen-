#Jeldrik Hemme#
#ETS 2021
#12.11.2021

#Hardware: wird nicht benötigt 

#Version:0.3

#Aufgabe: Schreiben Sie ein Programm, das mithilfe einer for-Schleife alle durch 9 teilbaren Zahlen zwischen zwei zuvor eingegebenen Grenzen
#in eine Liste schreibt und dann ausgibt.

#Eingabe der Werte 
unteregrenze = input('untere Grenze eingeben ')
oberegrenze = input('obere grenze eingeben ')

#Erstellen einer Variable für die Liste  
zahlenliste = []

#Erstellen der Liste und das Sortieren duch den Befehl append (hinzufügen von Werten in der) Liste
for zahlen in range (int(unteregrenze),int(oberegrenze)):
    if zahlen % 9 == 0:
        zahlenliste.append(zahlen)

#Erstellen der Liste zum Ausgeben 
for liste in zahlenliste:
    print(liste)

    
