__author__ = "Jakob Aungiers"
__copyright__ = "Jakob Aungiers 2018"
__version__ = "2.0.0"
__license__ = "MIT"

import os
import json
import time
import math
import matplotlib.pyplot as plt
from core.data_processor import DataLoader
from core.model import Model

import cleaner
import sys

configs = json.load(open('config.json', 'r'))

def plot_results(predicted_data, true_data):
    fig = plt.figure(facecolor='white')
    ax = fig.add_subplot(111)
    ax.plot(true_data, label='True Data')
    plt.plot(predicted_data, label='Prediction')
    plt.legend()
    plt.show()

def plot_results_multiple(predicted_data, true_data, prediction_len):
    fig = plt.figure(facecolor='white')
    ax = fig.add_subplot(111)
    ax.plot(true_data, label='True Data')
    #Pad the list of predictions to shift it in the graph to it's correct start
    for i, data in enumerate(predicted_data):
        padding = [None for p in range(i * prediction_len)]
        plt.plot(padding + data, label='Prediction')
    plt.legend()
    plt.show()

def main(choice):
    data = DataLoader(
        os.path.join('data', configs['data']['filename']),
        configs['data']['train_test_split'],
        configs['data']['columns']
    )
    model = Model()
    model.build_model(configs)
    if (choice != 'info'):
        x, y = data.get_train_data(
            seq_len = configs['data']['sequence_length'],
            normalise = configs['data']['normalise']
        )


        # in-memory training
        model.train(
        x,
        y,
        epochs = configs['training']['epochs'],
        batch_size = configs['training']['batch_size']
        )

        # out-of memory generative training
        # steps_per_epoch = math.ceil((data.len_train - configs['data']['sequence_length']) / configs['training']['batch_size'])
        # model.train_generator(
        #     data_gen = data.generate_train_batch(
        #         seq_len = configs['data']['sequence_length'],
        #         batch_size = configs['training']['batch_size'],
        #         normalise = configs['data']['normalise']
        #     ),
        #     epochs = configs['training']['epochs'],
        #     batch_size = configs['training']['batch_size'],
        #     steps_per_epoch = steps_per_epoch
        # )

        x_test, y_test = data.get_test_data(
            seq_len = configs['data']['sequence_length'],
            normalise = configs['data']['normalise']
        )

        if (choice == "multi"):
            predictions=model.predict_sequences_multiple(x_test,configs['data']['sequence_length'],configs['data']['sequence_length'])
            plot_results_multiple(predictions, y_test, configs['data']['sequence_length'])
        elif (choice == "seq"):
            predictions = model.predict_sequence_full(x_test, configs['data']['sequence_length'])
            plot_results(predictions, y_test)
        else:
            predictions = model.predict_point_by_point(x_test)
            plot_results(predictions, y_test)


if __name__=='__main__':
    # allows for multi, seq or point
    choice = sys.argv[1]
    if (choice == "multi" or choice == "seq" or choice == "point" or choice == "info"):
        main(choice)
    else:
        print("Please input a choice: multi, seq, point, info")

def predict(test):
    # initialize dataLoader with split of 0

    cleaner.main_func()

    data = DataLoader(
        test,
        0,
        configs['data']['columns']
    )
    x_test, y_test = data.get_test_data(
        seq_len = configs['data']['sequence_length'],
        normalise = False
    )
    model = Model()
    model.load_model('saved_models/tracker.h5')
    predictions = model.predict_point_by_point(x_test)
    plot_results(predictions, y_test)
    return "OK"
