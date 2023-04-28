# Deblur
# Language: C++
# Input: TXT
# Output: SAMPLE


Qiime2 deblur algorithm.

The plugin accepts as input a TXT file of tab-delimited keyword-value pairs:
inputfile: Sequences, typically already filtered
trimlength: Length to use for trimming sequences

The plugin produces as output three files, each in QZA format and beginning with the user-specified output samples:

samples-deblur-stats.qza: Statistics
samples-table.qza: Table of sequences
samples-rep-seqs.qza: Sequences after trimming
