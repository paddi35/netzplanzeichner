Es wird eine CSV-Datei im Format der Aufgabenstellung eingelesen und der fertige Netzplan in eine neue CSV oder PNG-Datei geschrieben. Wenn eine PNG-Datei als Ausgabedatei spezifiziert ist, wird eine Grafische Ausgabe des Netzplans erstellt. 


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

