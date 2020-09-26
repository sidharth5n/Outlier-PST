import argparse
from models import PST
from utils import *
import numpy as np

# Training settings
parser = argparse.ArgumentParser(description = 'Probabilistic Suffix Tree')
parser.add_argument('--dataset', type = str, required = True, help = 'Name of dataset file')
parser.add_argument('--dir', type = float, default = 'datasets/', help = 'Directory in which dataset is')
parser.add_argument('--size', type = float, default = 4, help = 'Length of buffer')
parser.add_argument('--k', type = float, default = 5, help = 'Cluster size')

args = parser.parse_args()

# Load labels for the data
labels = load_and_preprocess(dataset, dir, k)
# Instantiate a tree
tree = PST()
# Fit PST on the given data
tree.fit(labels, size)
# Display the tree
show(tree)
