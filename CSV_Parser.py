import csv
class CSV_Parser:
    #Liest CSV-Datei ein
    def __init__(self, filename,delimiter=';'):
        self.header = []
        self.rows = []
        file = open(filename)
        csvreader = csv.reader(file, delimiter=delimiter,skipinitialspace=True)
        #Kopfzeile einlesen
        self.header = next(csvreader)
        #Restliche Zeilen einlesen
        for row in csvreader:
            self.rows.append(row)