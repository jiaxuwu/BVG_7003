#!/usr/bin/env python3 

#Printing the tree object as a string at the entire object hierarchy
from Bio import Phylo 
tree = Phylo.read("simple.dnd", "newick")
print(tree)