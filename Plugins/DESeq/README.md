# DESeq
# Language: R
# Input: TXT 
# Output: CSV 

PluMA plugin to find the differentially abundant taxa between two groups.

The plugin takes as input a TXT file of keyword, value pairs, tab-delimited:
abundances: Taxa Count file
groups: Categories file consists of samples and group assignments.

The plugin will then output a CSV file of table of differentially abundant taxa along with their p-values,adjusted p-values, and fold change values of the two groups.
