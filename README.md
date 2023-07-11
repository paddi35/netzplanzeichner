# netzplanzeichner

## benötigte Bibliotheken (in Admin-CMD ausführen)
1. pip install typing-extensions
2. pip install opencv-python
3. pip install Pillow==9.0.0 

## Ausführung (siehe auch weiter unten)
`python "C:\Users\pvo\Downloads\netzplanzeichner-main\main.py" "C:\Users\pvo\Downloads\netzplanzeichner-main\input_nachfolger_fom.csv" "C:\Users\pvo\Downloads\netzplanzeichner-main\output_netplan.png"`

-> Ruft das `main.py` Skript aus und übergibt eine CSV-Datei mit "Nachfolgern" (analog Vorlesung) und übergibt dann den Dateipfad, wo der Netzplan gespeichert wird.

## Knoteninformation

![knoten_info](https://github.com/paddi35/netzplanzeichner/assets/79044236/143c913c-8e88-4ffc-8925-0d41c2cfdcef)

- FAZ: frühster Anfangszeitpunkt (oben links)
- FEZ: frühster Endzeitpunkt (oben rechts)
- SAZ: spätester Anfangszeitpunkt (unten links)
- SEZ: spätester Endzeitpunkt (unten rechts)
- ID: oberen beiden Felder
- Dauer: Dauer (unten linkes Feld)
- GP:  gesamter Puffer (unten mittleres Feld)
- FP: freier Puffer (unten rechtes Feld)


## Original
Es wird eine CSV-Datei im Format der Dateien im Verzeichnis Test/inputs eingelesen und der fertige Netzplan in eine neue CSV oder PNG-Datei geschrieben. Wenn eine PNG-Datei als Ausgabedatei angegeben ist, wird eine Grafische Ausgabe des Netzplans erstellt. 


Ausführung des Programms:

python3 main.py [Eingabedatei] [Ausgabedatei]


Positivtests:

python3 main.py Test/inputs/Positivtests/input_n.csv Test/outputs/output_n.csv
python3 main.py Test/inputs/Positivtests/input_v.csv Test/outputs/output_v.csv
python3 main.py Test/inputs/Positivtests/zwei_endpunkte.csv Test/outputs/zwei_endpunkte.csv
python3 main.py Test/inputs/Positivtests/input_n.csv Test/outputs/output_n.png
python3 main.py Test/inputs/Positivtests/input_v.csv Test/outputs/output_v.png
python3 main.py Test/inputs/Positivtests/zwei_endpunkte.csv Test/outputs/zwei_endpunkte.png

Negtativtests:

python3 main.py Test/inputs/Negativtests/input_buchstabe_dauer.csv Test/outputs/output.csv
python3 main.py Test/inputs/Negativtests/input_buchstabe_nr.csv Test/outputs/output.csv
python3 main.py Test/inputs/Negativtests/input_dauer_negativ.csv Test/outputs/output.csv
python3 main.py Test/inputs/Negativtests/input_mehrmals_selbe_nr.csv Test/outputs/output.csv
python3 main.py Test/inputs/Negativtests/input_nr_negativ.csv Test/outputs/output.csv
python3 main.py Test/inputs/Negativtests/zyklus.csv Test/outputs/output.csv

