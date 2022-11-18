#!/usr/bin/env python3

# use the function "draw" to create a simple graphic dendrogram
from Bio import Phylo
tree = Phylo.read("simple.dnd", "newick")
tree.rooted = True
Phylo.draw(tree)