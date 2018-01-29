#!/usr/bin/env python

"""
Script accepts MSA from cmsearch and outputs the RNA sequences
"""

__author__ = "Paul Donovan" 
__maintainer__ = "Paul Donovan"
__email__ = "pauldonovandonegal@gmail.com"

import sys

#Display help and usage
parser = argparse.ArgumentParser(description="Incorrect number of command line arguments")
parser.add_argument('Input.tsv')
parser.add_argument('Output.tsv')
if len(sys.argv[1:]) == 0:
    parser.print_help()
    parser.exit()
args = parser.parse_args()

File_Read = list(line.strip().split("\t") for line in open(sys.argv[1]))
count = 0
for items in File_Read:
    if items[0].startswith("#"):
        pass
    else:
        if items[0].startswith("//"):
            pass
        else:
            count = count + 1
            Riboswitch = items[0].replace("/","_")
            RNA = items[1].replace("-", "")
            RNA = RNA.replace(".","")
            File_out = open(sys.argv[2] + "_" + str(Riboswitch) + ".fsa", "w")
            File_out.write(RNA + "\n")
            File_out.close()