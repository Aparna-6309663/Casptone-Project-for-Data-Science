import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

class RFPlugin:
    def input(self, inputfile):
        global parameters, data_train, data_test, ytrain
        parameters = pd.read_csv(inputfile, sep="\t", header=None, index_col=0, squeeze=True)
        if 'training' in parameters:
            data_train = pd.read_csv(parameters['training'], index_col=0)
            print("Training data loaded")
        else:
            print("Error: 'training' not found in parameters")
        if 'testing' in parameters:
            data_test = pd.read_csv(parameters['testing'], index_col=0)
            print("Testing data loaded")
        else:
            print("Error: 'testing' not found in parameters")
        if 'traininggroups' in parameters:
            ytrain = np.loadtxt(parameters['traininggroups'], delimiter=',')
            print("Training labels loaded")
        else:
            print("Error: 'traininggroups' not found in parameters")

    def run(self):
        global data_train, data_test, ytrain, pred
        if 'data_train' not in globals():
            print("Error: data_train not defined")
            pred = np.array([])
            return
        try:
            if not data_train.empty:
                # Remove zero columns
                data_train = data_train.loc[:, (data_train != 0).any(axis=0)]
                data_test = data_test.loc[:, (data_test != 0).any(axis=0)]

                # Define the model architecture
                model = RandomForestClassifier(n_estimators=2000, max_depth=66)

                # Fit the model to the training data
                model.fit(data_train, ytrain)

                # Predict on test set
                pred = model.predict(data_test)
            else:
                pred = np.array([])
        except NameError:
            print("Error: data_train not defined")
            pred = np.array([])

    def output(self, outputfile):
        global pred
        np.savetxt(outputfile, pred, delimiter=",")
