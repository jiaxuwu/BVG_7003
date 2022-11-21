# BVG_7003_Biopython

This page is created by Jiaxu Wu

There are some python scripts for test in BVG_7003 @ Université Laval, including `Bio.Seq` and `Bio.Phylo` two parts.

For Bio.SeqIO --see https://biopython.org/wiki/SeqIO

For Bio.Phylo --see https://biopython.org/wiki/Phylo

The Biopython Project is an international association of developers of freely available Python tools for computational molecular biology.
The goal of Biopython is to make it as easy as possible to use Python for bioinformatics by creating high-quality, reusable modules and classes. Biopython features include parsers for various Bioinformatics file formats (BLAST, Clustalw, FASTA, Genbank,…), access to online services (NCBI, Expasy,…), interfaces to common and not-so-common programs (Clustalw, DSSP, MSMS…), a standard sequence class, various clustering modules, a KD tree data structure etc. and even documentation.

## Requirement

**Python 3.7 or later** --see http://www.python.org 


## Biophyton installation

    pip3 install biopython
  
To check the function if Biopython is working in python3:

    >>> import Bio
    >>> print(Bio.__version___)
    
Usage
-------

    ./filename.py
    
or

    python3 filename.py

Bio.SeqIO 
----------

Bio.SeqIO provides a simple uniform interface to input/output assorted sequence file formats.

There are 9 expamles in this section. We also attached `NC_000913.faa`, `NC_000913.gbk`, `NC_000913_cds.fasta` and `PGSC_DM_v3.4_pep_representative.fasta` as testfiles. 

### Examples

`count_fasta.py` is used for to count fasta records from `NC_000913.faa` file. 

>The output is:
>`There are 4140 records in file NC_000913.faa`

`count_record.py` is used to print all the 4140 ID of `NC_000913.faa` file and their length.

`check_start_met.py` is used to check the numbers of protein do not start with methionine from `NC_000913.faa`.

>The output is:
>Found 0 records in filename which did not start with M

`check_start_met1.py` is used to print and check the numbers of protein do not start with methionine from `PGSC_DM_v3.4_pep_representative.fasta`.

>The output is:
>Found 208 records in PGSC_DM_v3.4_pep_representative.fasta which did not start with M

`convert.py` is used to convert a sequence file from `.gbk (NC_000913.gbk)` to `.fasta (NC_000913_converted.fasta)` file.

>The output is:
>1 records converted

`filter.py` is used to filter the sequence less than 100 amino acids long from `NC_000913.faa`.

>The output is:
>3720 records selected out of 4140

`edit.py` is used to edit sequence (take everything up to but excluding the final letter) from `PGSC_DM_v3.4_pep_representative.fasta`.

>The new file will be created:
>`PGSC_DM_v3.4_pep_rep_no_stars.fasta`

`filter2.py` is used to select selects records of type CDS from NC_000913.gbk and creat a file named `NC_000913_cds.fasta`.

>The output is:
>4319 CDS sequences extracted

`total_gene_lengths` is used stelect gene type features  and calculates the total length including all genes from `NC_000913.gbk`.

>The output is:
>Total length of all genes is 4137209

Bio.Phylo 
----------

Bio.Phylo provides classes, functions and I/O support for working with phylogenetic trees.

There are 3 examples in this section. We also attached `simple.dnd` as the test file.

### Examples

`phylogenetic_1` is used to print the tree object as a string gives us a look at the entire object hierarchy.

`phylogenetic_2` is used to create a simple ASCII-art (plain text) dendrogram.

`phylogenetic_3` is used to draw a graphic dendrogram (should install `matplotlib` or `pylab` before using).




