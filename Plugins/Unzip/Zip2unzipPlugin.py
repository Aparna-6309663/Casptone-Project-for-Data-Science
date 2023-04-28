import zipfile
import os

# Defining input function
class Zip2unzipPlugin:
    def input(self,filename):
            self.Zipfile = open(filename,'rb')


    def run(self):
        # Create output directory if it does not exist
        outdir = "/lclhome/aviru002/PluMA/pipelines/Parkinsons/CSV"
        if not os.path.exists(outdir):
            os.makedirs(outdir)

        # Extract all files from the zip archive to the output directory
        with zipfile.ZipFile(self.Zipfile, 'r') as zip:
            zip.extractall(outdir)

    def output(self, filename):
        with open(filename, 'w') as f:
            f.write('File unzipped successfully')
