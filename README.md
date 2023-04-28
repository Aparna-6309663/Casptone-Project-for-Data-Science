# Casptone-Project-for-Data-Science
# General purpose microbiome pipeline applied to Parkinson's dataset

This repository contains a general purpose microbiome pipeline that has been applied to the Parkinson's disease dataset. The pipeline consists of various plugins that have been used to analyze the microbiome data obtained from patients with Parkinson's disease and control subjects.

The pipeline consists of the following plugins:

FASTQ2QZA* - This plugin is used to convert the raw FASTQ files to QZA format for further analysis.

Quality Filter* - This plugin is used to filter out poor quality reads that may affect downstream analysis.

Deblur* - This plugin is used to denoise the sequences and remove any chimeric sequences.

Feature Classify* - This plugin is used to assign taxonomic assignments to the denoised sequences using a trained classifier(SILVA).

DESeq* - This plugin is used to perform differential abundance analysis between the groups (Parkinson's and control).

Phyloseqglom* - This plugin is used to summarize the abundances of microbial taxa at Family Level.

Standard Scalar Method - This plugin is used to scale the data prior to feeding into machine learning models.

Data Split- This plugin is used to split the data into training and testing sets for machine learning models.

ML models - This plugin is used to train machine learning models (random forests, SVM, Neural Network) to predict the labels on test data.

The pipeline is tested on 35 samples, but it can be easily expanded to handle larger datasets by adding more FASTQ files and expanding the manifest.

* - Existed Plugins.


