#!/usr/bin/env python3

# use function "draw_ascii" to create simple ascii-art dendrogram
from Bio import Phylo
tree = Phylo.read("simple.dnd", "newick")
Phylo.draw_ascii(tree)