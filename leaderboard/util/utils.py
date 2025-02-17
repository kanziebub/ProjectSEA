import math
import yaml


def read_yaml(filepath):
    with open(filepath, "r") as f:
        data = yaml.load(f, Loader=yaml.SafeLoader)
    return data


def check_int(value):
    return 0 if math.isnan(value) else int(value)


def check_str(value):
    return "" if math.isnan(value) else str(value)
