#This file will contain utility functions for:
#Loading and saving JSON files
# Normalizing text for case-insensitive matching

import json
import os

def load_data(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as f:
        return json.load(f)

def save_data(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def normalize(text):
    return text.strip().lower()