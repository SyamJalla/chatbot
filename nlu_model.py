import logging
import pprint
import rasa_nlu
from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Interpreter
from rasa_nlu.test import run_evaluation


logfile = 'nlu_model.log'

import pandas as pd

class_csv = pd.read_csv('./classes_in_imagenet.csv')
# print(class_csv.head(5))


def train_nlu(data_path, configs, model_path):
    logging.basicConfig(filename=logfile, level=logging.DEBUG)
    training_data = load_data(data_path)
    trainer = Trainer(config.load(configs))
    trainer.train(training_data)
    model_directory = trainer.persist(model_path, project_name='current', fixed_model_name='nlu')
    run_evaluation(data_path, model_directory)


def run_nlu(nlu_path):
    logging.basicConfig(filename=logfile, level=logging.DEBUG)
    interpreter = Interpreter.load(nlu_path)
    # pprint.pprint(interpreter.parse("Share some latest news around the world?"))
    # pprint.pprint(interpreter.parse("What is meant by in artificial intelligence?"))
    # pprint.pprint(interpreter.parse("What is meant by machine learning?"))
    # pprint.pprint(interpreter.parse("Share some latest news around the world?"))
    # pprint.pprint(interpreter.parse("What is going on in technology?"))
    # pprint.pprint(interpreter.parse("What is going on in education?"))
    # pprint.pprint(interpreter.parse("Hola"))
    # pprint.pprint(interpreter.parse("ola"))
    pprint.pprint(interpreter.parse("Programming Language"))
    pprint.pprint(interpreter.parse("program"))
    pprint.pprint(interpreter.parse("Project"))
    # pprint.pprint(interpreter.parse("Sprite"))
    # pprint.pprint(interpreter.parse("How to give instructions to the computer"))
    # pprint.pprint(interpreter.parse("What is scratch program"))
    # pprint.pprint(interpreter.parse("How to add sprite"))
    # pprint.pprint(interpreter.parse("How to add costume"))
    # pprint.pprint(interpreter.parse("Test me"))

    for i in range(0, 21840):
        print(class_csv['class_name'][i])
        pprint.pprint(interpreter.parse(str(class_csv['class_name'][i])))


if __name__ == '__main__':
    train_nlu('./data/nlu.md', 'nlu_config.yml', './models')
    run_nlu('./models/current/nlu')