#!/usr/bin/env python3

# Use Bio.Seq to count record
from Bio import SeqIO
filename = "NC_000913.faa" # Write your file name here
for record in SeqIO.parse(filename, "fasta"):
    print("Record " + record.id + "length " + str(len(record.seq)))
