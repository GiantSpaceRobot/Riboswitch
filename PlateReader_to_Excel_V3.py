#!/usr/bin/env python

"""
Very messy script that accepts raw plate reader (Synergy HT) output and formats it so it is ready for R or excel
"""

__author__ = "Paul Donovan" 
__maintainer__ = "Paul Donovan"
__email__ = "pauldonovandonegal@gmail.com"

import os
from itertools import izip
import sys
from collections import OrderedDict
import csv

#Display help and usage
parser = argparse.ArgumentParser(description="Incorrect number of command line arguments")
parser.add_argument('Raw-platereader-output.txt')
parser.add_argument('Row-and-Column-Names.txt')
parser.add_argument('Reformatted.tsv')
if len(sys.argv[1:]) == 0:
    parser.print_help()
    parser.exit()
args = parser.parse_args()

POP = open(sys.argv[1], "r")
FILE = POP.readlines()
POP.close()

Plate = open(sys.argv[2], "r")
PlateLayout = Plate.readlines()
Plate.close()

Time = list()

A1_List = list()
A2_List = list()
A3_List = list()
A4_List = list()
A5_List = list()
A6_List = list()
A7_List = list()
A8_List = list()
A9_List = list()
A10_List = list()
A11_List = list()
A12_List = list()

B1_List = list()
B2_List = list()
B3_List = list()
B4_List = list()
B5_List = list()
B6_List = list()
B7_List = list()
B8_List = list()
B9_List = list()
B10_List = list()
B11_List = list()
B12_List = list()

C1_List = list()
C2_List = list()
C3_List = list()
C4_List = list()
C5_List = list()
C6_List = list()
C7_List = list()
C8_List = list()
C9_List = list()
C10_List = list()
C11_List = list()
C12_List = list()

D1_List = list()
D2_List = list()
D3_List = list()
D4_List = list()
D5_List = list()
D6_List = list()
D7_List = list()
D8_List = list()
D9_List = list()
D10_List = list()
D11_List = list()
D12_List = list()

E1_List = list()
E2_List = list()
E3_List = list()
E4_List = list()
E5_List = list()
E6_List = list()
E7_List = list()
E8_List = list()
E9_List = list()
E10_List = list()
E11_List = list()
E12_List = list()

F1_List = list()
F2_List = list()
F3_List = list()
F4_List = list()
F5_List = list()
F6_List = list()
F7_List = list()
F8_List = list()
F9_List = list()
F10_List = list()
F11_List = list()
F12_List = list()

G1_List = list()
G2_List = list()
G3_List = list()
G4_List = list()
G5_List = list()
G6_List = list()
G7_List = list()
G8_List = list()
G9_List = list()
G10_List = list()
G11_List = list()
G12_List = list()

H1_List = list()
H2_List = list()
H3_List = list()
H4_List = list()
H5_List = list()
H6_List = list()
H7_List = list()
H8_List = list()
H9_List = list()
H10_List = list()
H11_List = list()
H12_List = list()

Dic = dict()

def Well_Data(Row):
    if line.startswith(Row):
        for idx, val in enumerate(Readings):  #Access index and value
            well_ID = (Row + str(idx + 1))  #Get well ID (e.g. A1, A2 etc.)
            for i in range(113):
                if well_ID == (str(Row) + str(i)):
                    if well_ID == "A1":
                        A1_List.append(val)
                    if well_ID == "A2":
                        A2_List.append(val)
                    if well_ID == "A3":
                        A3_List.append(val)
                    if well_ID == "A4":
                        A4_List.append(val)
                    if well_ID == "A5":
                        A5_List.append(val)
                    if well_ID == "A6":
                        A6_List.append(val)
                    if well_ID == "A7":
                        A7_List.append(val)
                    if well_ID == "A8":
                        A8_List.append(val)
                    if well_ID == "A9":
                        A9_List.append(val)
                    if well_ID == "A10":
                        A10_List.append(val)
                    if well_ID == "A11":
                        A11_List.append(val)
                    if well_ID == "A12":
                        A12_List.append(val)
                    if well_ID == "B1":
                        B1_List.append(val)
                    if well_ID == "B2":
                        B2_List.append(val)
                    if well_ID == "B3":
                        B3_List.append(val)
                    if well_ID == "B4":
                        B4_List.append(val)
                    if well_ID == "B5":
                        B5_List.append(val)
                    if well_ID == "B6":
                        B6_List.append(val)
                    if well_ID == "B7":
                        B7_List.append(val)
                    if well_ID == "B8":
                        B8_List.append(val)
                    if well_ID == "B9":
                        B9_List.append(val)
                    if well_ID == "B10":
                        B10_List.append(val)
                    if well_ID == "B11":
                        B11_List.append(val)
                    if well_ID == "B12":
                        B12_List.append(val)
                    if well_ID == "C1":
                        C1_List.append(val)
                    if well_ID == "C2":
                        C2_List.append(val)
                    if well_ID == "C3":
                        C3_List.append(val)
                    if well_ID == "C4":
                        C4_List.append(val)
                    if well_ID == "C5":
                        C5_List.append(val)
                    if well_ID == "C6":
                        C6_List.append(val)
                    if well_ID == "C7":
                        C7_List.append(val)
                    if well_ID == "C8":
                        C8_List.append(val)
                    if well_ID == "C9":
                        C9_List.append(val)
                    if well_ID == "C10":
                        C10_List.append(val)
                    if well_ID == "C11":
                        C11_List.append(val)
                    if well_ID == "C12":
                        C12_List.append(val)
                    if well_ID == "D1":
                        D1_List.append(val)
                    if well_ID == "D2":
                        D2_List.append(val)
                    if well_ID == "D3":
                        D3_List.append(val)
                    if well_ID == "D4":
                        D4_List.append(val)
                    if well_ID == "D5":
                        D5_List.append(val)
                    if well_ID == "D6":
                        D6_List.append(val)
                    if well_ID == "D7":
                        D7_List.append(val)
                    if well_ID == "D8":
                        D8_List.append(val)
                    if well_ID == "D9":
                        D9_List.append(val)
                    if well_ID == "D10":
                        D10_List.append(val)
                    if well_ID == "D11":
                        D11_List.append(val)
                    if well_ID == "D12":
                        D12_List.append(val)
                    if well_ID == "E1":
                        E1_List.append(val)
                    if well_ID == "E2":
                        E2_List.append(val)
                    if well_ID == "E3":
                        E3_List.append(val)
                    if well_ID == "E4":
                        E4_List.append(val)
                    if well_ID == "E5":
                        E5_List.append(val)
                    if well_ID == "E6":
                        E6_List.append(val)
                    if well_ID == "E7":
                        E7_List.append(val)
                    if well_ID == "E8":
                        E8_List.append(val)
                    if well_ID == "E9":
                        E9_List.append(val)
                    if well_ID == "E10":
                        E10_List.append(val)
                    if well_ID == "E11":
                        E11_List.append(val)
                    if well_ID == "E12":
                        E12_List.append(val)
                    if well_ID == "F1":
                        F1_List.append(val)
                    if well_ID == "F2":
                        F2_List.append(val)
                    if well_ID == "F3":
                        F3_List.append(val)
                    if well_ID == "F4":
                        F4_List.append(val)
                    if well_ID == "F5":
                        F5_List.append(val)
                    if well_ID == "F6":
                        F6_List.append(val)
                    if well_ID == "F7":
                        F7_List.append(val)
                    if well_ID == "F8":
                        F8_List.append(val)
                    if well_ID == "F9":
                        F9_List.append(val)
                    if well_ID == "F10":
                        F10_List.append(val)
                    if well_ID == "F11":
                        F11_List.append(val)
                    if well_ID == "F12":
                        F12_List.append(val)
                    if well_ID == "G1":
                        G1_List.append(val)
                    if well_ID == "G2":
                        G2_List.append(val)
                    if well_ID == "G3":
                        G3_List.append(val)
                    if well_ID == "G4":
                        G4_List.append(val)
                    if well_ID == "G5":
                        G5_List.append(val)
                    if well_ID == "G6":
                        G6_List.append(val)
                    if well_ID == "G7":
                        G7_List.append(val)
                    if well_ID == "G8":
                        G8_List.append(val)
                    if well_ID == "G9":
                        G9_List.append(val)
                    if well_ID == "G10":
                        G10_List.append(val)
                    if well_ID == "G11":
                        G11_List.append(val)
                    if well_ID == "G12":
                        G12_List.append(val)
                    if well_ID == "H1":
                        H1_List.append(val)
                    if well_ID == "H2":
                        H2_List.append(val)
                    if well_ID == "H3":
                        H3_List.append(val)
                    if well_ID == "H4":
                        H4_List.append(val)
                    if well_ID == "H5":
                        H5_List.append(val)
                    if well_ID == "H6":
                        H6_List.append(val)
                    if well_ID == "H7":
                        H7_List.append(val)
                    if well_ID == "H8":
                        H8_List.append(val)
                    if well_ID == "H9":
                        H9_List.append(val)
                    if well_ID == "H10":
                        H10_List.append(val)
                    if well_ID == "H11":
                        H11_List.append(val)
                    if well_ID == "H12":
                        H12_List.append(val)

Rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

for line in FILE: 
    LS = line.strip().split()
    if "Kinetic" in line:
        time = line.split("(")
        time = time[1].split(")")
        time = time[0]
        Time.append(time)
    else:
        Readings = LS[1:13]
        for Row in Rows:
            Well_Data(Row)

lis = [Time, A1_List, A2_List, A3_List, A4_List, A5_List, A6_List, A7_List, A8_List, A9_List, A10_List, A11_List, A12_List, 
        B1_List, B2_List, B3_List, B4_List, B5_List, B6_List, B7_List, B8_List, B9_List, B10_List, B11_List, B12_List, 
        C1_List, C2_List, C3_List, C4_List, C5_List, C6_List, C7_List, C8_List, C9_List, C10_List, C11_List, C12_List, 
        D1_List, D2_List, D3_List, D4_List, D5_List, D6_List, D7_List, D8_List, D9_List, D10_List, D11_List, D12_List, 
        E1_List, E2_List, E3_List, E4_List, E5_List, E6_List, E7_List, E8_List, E9_List, E10_List, E11_List, E12_List, 
        F1_List, F2_List, F3_List, F4_List, F5_List, F6_List, F7_List, F8_List, F9_List, F10_List, F11_List, F12_List, 
        G1_List, G2_List, G3_List, G4_List, G5_List, G6_List, G7_List, G8_List, G9_List, G10_List, G11_List, G12_List, 
        H1_List, H2_List, H3_List, H4_List, H5_List, H6_List, H7_List, H8_List, H9_List, H10_List, H11_List, H12_List]

with open("intermediate-file.csv", "wb") as f: #Write .csv file with all lists of OD600 values
    writer = csv.writer(f)
    writer.writerows(lis)

a = izip(*csv.reader(open("intermediate-file.csv", "rb"))) #Read in .csv file and change columns to rows (zip function)
csv.writer(open("intermediate-file2.csv", "wb")).writerows(a)

#Make the header for the final file
Header = ("A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "A11", "A12", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10", "B11", "B12", "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10", "D11", "D12", "E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9", "E10", "E11", "E12", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12", "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "G10", "G11", "G12", "H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11", "H12")

RowNames = PlateLayout[0].strip().split("\t")
RowSplit = list()
RowLetter = list()
RowSpecies = list()
for i in RowNames:
    i = i.strip().split("__")
    RowLetter.append(i[0])
    RowSpecies.append(i[1])

ColumnNames = PlateLayout[1].strip().split("\t")
ColumnNumber = list()
ColumnConc = list()
for i in ColumnNames:
    i = i.strip().split("__")
    ColumnNumber.append(i[0])
    ColumnConc.append(i[1])

HeaderList = list()
Switch = 0
for i in Header:  #Map the well IDs to the species/concentrations 
    for letter in RowLetter:
        if letter in i:
            RowIndex = RowLetter.index(letter)
            Species = RowSpecies[RowIndex]
            for number in ColumnNumber:
                if number in i:
                    ColumnIndex = ColumnNumber.index(number)    
                    Conc = ColumnConc[ColumnIndex]
                    Switch = 1
    if Switch == 1:
        HeaderList.append(str(Species) + " " + str(Conc)) 
        Switch = 0

with open("intermediate-file2.csv", 'r') as fin, open((sys.argv[3]), 'w') as fout:
    fout.write("Time")
    for i in HeaderList:
        fout.write("\t" + str(i))
    fout.write("\n")
    for line in fin:
        item = line.strip().split(",")
        fout.write("\t".join(item) + "\n")



