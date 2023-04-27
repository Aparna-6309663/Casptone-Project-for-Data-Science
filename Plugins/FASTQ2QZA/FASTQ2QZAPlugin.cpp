#include "PluginManager.h"
#include <stdio.h>
#include <stdlib.h>
#include "FASTQ2QZAPlugin.h"

void FASTQ2QZAPlugin::input(std::string file) {
    inputfile = file;
    std::ifstream ifile(inputfile.c_str(), std::ios::in);
    while (!ifile.eof()) {
        std::string key, value;
        ifile >> key;
        ifile >> value;
        parameters[key] = value;
    }
}

void FASTQ2QZAPlugin::run() {
    // Determine the input type based on the presence of the _R1 or _R2 suffix in the input file names
    bool is_paired_end = false;
    if (inputfile.find("_R1") != std::string::npos || inputfile.find("_R2") != std::string::npos) {
        is_paired_end = true;
    }

    std::string command = "export OLDPATH=${PATH}; ";
    command += "export PATH=${CONDA_HOME}/bin/:${PATH}; ";
    command += "eval \"$(conda shell.bash hook)\"; ";
    command += "conda activate qiime2-2021.4; ";

    if (is_paired_end) {
        command += "qiime tools import --type 'SampleData[PairedEndSequencesWithQuality]' --input-path "+std::string(PluginManager::prefix())+"/"+parameters["manifest"]+" --output-path "+std::string(PluginManager::prefix())+"/"+parameters["output"]+" --input-format "+parameters["format"]+"; ";
    } else {
        command += "qiime tools import --type 'SampleData[SequencesWithQuality]' --input-path "+std::string(PluginManager::prefix())+"/"+parameters["manifest"]+" --output-path "+std::string(PluginManager::prefix())+"/"+parameters["output"]+" --input-format "+parameters["format"]+"; ";
    }

    command += "conda deactivate; ";
    command += "conda deactivate; ";
    command += "export PATH=${OLDPATH}";
    std::cout << command << std::endl;

    system(command.c_str());
}

void FASTQ2QZAPlugin::output(std::string file) {
}

PluginProxy<FASTQ2QZAPlugin> FASTQ2QZAPluginProxy = PluginProxy<FASTQ2QZAPlugin>("FASTQ2QZA", PluginManager::getInstance());

