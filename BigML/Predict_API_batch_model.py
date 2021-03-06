from bigml.model import Model
from bigml.api import BigML
import bigml.util as util
import glob
import os
import csv 
import json

from models import models, black_box_models


# from models import models, black_box_models
MODEL_STORAGE = './data/BigML_models'
DATASET_STORAGE = './data/datasets'
PREDICT_STORAGE = './data/predict_result'

BB_KEY = "ce4f274a13375e6ffa0c4b321761dd67376cf435"
BB_USER_NAME = "HowardChao"
BB_KEY = "ce4f274a13375e6ffa0c4b321761dd67376cf435"

def main():
    pass

def test_online_model(model_name):
    
    # Create local_model object
    print("Creating model from API .... ")

    predict_storage = os.path.join(PREDICT_STORAGE, model_name)
    if not os.path.exists(predict_storage):
        print("Creating predict directory .... ")
        os.makedirs(predict_storage)
    API_predict_storage = os.path.join(predict_storage, "API_result")
    if not os.path.exists(API_predict_storage):
        print("Creating predict directory .... ")
        os.makedirs(API_predict_storage)
    api = BigML(storage=API_predict_storage)
    print("Reading testing data .... ")
    test_source = api.create_source(os.path.join(DATASET_STORAGE, model_name, model_name+"_test.csv"))
    api.ok(test_source)
    test_dataset = api.create_dataset(test_source)
    api.ok(test_dataset)
    print("Start predicting .... ")
    if which_model == "DT":
        batch_prediction = api.create_batch_prediction('model/{}'.format(models[model_name]), test_dataset, {"all_fields": True, "probabilities": True})
    elif which_model == "DN":
        batch_prediction = api.create_batch_prediction('deepnet/{}'.format(models[model_name]), test_dataset, {"all_fields": True, "probabilities": True})
    api.ok(batch_prediction)
    print(batch_prediction)
    api.download_batch_prediction(batch_prediction, filename=os.path.join(predict_storage, model_name + "_results"))
    print("Finish batch prediction !!")


if __name__ == "__main__":
    main()
    model_name = input('Enter a model name: ')
    which_model = input('Which model are u going to predict (Decision tree / Deepnet)? ')
    test_online_model(model_name)