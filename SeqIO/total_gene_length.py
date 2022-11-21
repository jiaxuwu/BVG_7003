#!/usr/bin/env python3

# Looking for gene records, and calculate their total length
from Bio import SeqIO
record = SeqIO.read("NC_000913.gbk", "genbank")
total = 0
for feature in record.features:
    if feature.type == "gene":
        total = total + len(feature)
print("Total length of all genes is " + str(total))