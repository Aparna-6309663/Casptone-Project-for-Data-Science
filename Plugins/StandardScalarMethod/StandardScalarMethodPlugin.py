# Import necessary libraries
from sklearn.preprocessing import StandardScaler
import pandas as pd

#Defining Plugin Class 
class StandardScalarMethodPlugin:

    #Defining input function
    def input(self, filename):

        # Reading input data as a pandas DataFrame
        self.data = pd.read_csv(filename, index_col=0)

    # Defining run function
    def run(self):

        # Initializing StandardScaler object
        scaler = StandardScaler()

        # Fitting and transforming data using StandardScaler Method
        self.normalized_data = pd.DataFrame(scaler.fit_transform(self.data),index=self.data.index,columns=self.data.columns)

    # Defining output function
    def output(self, filename):

        #Writing normalized data to output file
        self.normalized_data.to_csv(filename)
