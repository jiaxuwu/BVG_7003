#!/usr/bin/env python3

# Using Bio.SeqIO to count fasta files
from Bio import SeqIO
filename = "NC_000913.faa"
count = 0
for record in SeqIO.parse (filename, "fasta"):
    count = count +1

print ("There are " + str(count) + " records in file " + filename)




