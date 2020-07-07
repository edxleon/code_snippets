import os
import glob
from collections import OrderedDict
import json

# Read the entire file as a single string

sample_file = './zeilen.txt'


def read_file(filename):
    with open(filename, 'rt') as f:
        data = f.read()
    return data


def get_all_files(dirname):
    return [name for name in os.listdir(dirname)
            if os.path.isfile(os.path.join(dirname, name))]


def get_all_dirs(dirname):
    return [name for name in os.listdir(dirname)
            if os.path.isdir(os.path.join(dirname, name))]


def get_all_files_endswith(dirname, end):
    return [name for name in os.listdir(dirname) if name.endswith(end)]


def get_all_files_matching(mathstring):
    return glob.glob(mathstring)
