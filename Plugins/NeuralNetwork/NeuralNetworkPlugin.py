import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

class NeuralNetworkPlugin:
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
                model = Sequential()
                model.add(Dense(180, activation='relu', input_shape=(data_train.shape[1],)))
                model.add(Dense(90, activation='relu'))
                model.add(Dense(45, activation='relu'))
                model.add(Dense(1, activation='sigmoid'))

                # Compile the model
                model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

                # Fit the model to the training data
                model.fit(data_train, ytrain, epochs=10, batch_size=32)

                # Predict on test set
                pred = model.predict_classes(data_test).ravel()
            else:
                pred = np.array([])
        except NameError:
            print("Error: data_train not defined")
            pred = np.array([])

    def output(self, outputfile):
        global pred
        np.savetxt(outputfile, pred, delimiter=",")

