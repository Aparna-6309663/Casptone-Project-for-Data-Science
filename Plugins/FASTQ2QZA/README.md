# FASTQ2QZA
# Language: C++
# Input: TXT
# Output: QZA

PluMA plugin to convert multiple FASTQ files into a single QZA file for Qiime 2.

Output file will be in QZA format.  The input file is a TXT file of tab-delimited keyword-value pairs:

manifest: Manifest file containing sequence names and absolute pathnames for forward and reverse sequence files

format: Format used for manifest for  Paired End - PairedEndFastqManifestPhred33V2 
                                      Single End- SingleEndFastqManifestPhred33V2
