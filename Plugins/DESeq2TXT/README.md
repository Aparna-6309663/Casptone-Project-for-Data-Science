# DESeq2TXT
# Language: Python
# Input: TXT
# Output: TXT

PluMA plugin that takes the output of DESeq
and does two things:
1. p-value thresholds the data (user-specified p-value)
2. Allows the user to specify the two groups

It produces a human-readable text file with differentially abundant
taxa that have passed the p-value check, and the group that each
distinguish.

The plugin accepts as input a parameter file of keyword-value pairs:
taxa: Taxa file
deseq: DESeq output CSV
group1: Name of first group- Parkinsons
group2: Name of second group- Control
pvalue: P-Value threshold
