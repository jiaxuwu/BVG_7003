#!/usr/bin/env python3

# Checking proteins start without methionine
from Bio import SeqIO
filename = "NC_000913.faa"  # Write your file name here
bad = 0
for record in SeqIO.parse(filename, "fasta"):
    if not record.seq.startswith("M"):
        bad = bad + 1
        print(record.id + " starts " + record.seq(0))
print("Found " + str(bad) + " records in " + "filename" + " which did not start with M")
