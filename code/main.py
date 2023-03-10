import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from yellowbrick.classifier import ConfusionMatrix

from models.dev import Developer, get_dev_by_name
from models.instance import Instance
from models.task import Task


def main():
    instances: list[Instance] = []
    d = get_dev_by_name("CARLOS_AMARAL")

    return


main()
