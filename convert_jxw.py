#!/usr/bin/env python3

# Converting a sequence file from .gbk to .fasta file
from Bio import SeqIO
input_filename = "NC_000913.gbk"  # Write the .gbk file name here
output_filename = "NC_000913_converted.fasta"
count = SeqIO.convert(input_filename, "gb", output_filename, "fasta")
print(str(count) + " records converted")

