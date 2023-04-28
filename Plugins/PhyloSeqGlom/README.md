# PhyloSeqGlom
# Language: R
# Input: TXT
# Output: DIR

PluMA plugin that takes PhyloSeq and extracts a specific taxonomic level. Here is at Family Level.
The plugin accepts as input a parameter file of keyword-value pairs.  Abundances and taxonomy are formatted according to PhyloSeq:

OTU: otu.csv
META: output.meta.csv
TREE: asv.taxonomy.csv
LEVEL: Taxonomic level (Family Level)

Modified PhyloSeq data is output to the user-specified directory.
