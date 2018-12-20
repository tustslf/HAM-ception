from __future__ import print_function, division
import random
import os
import numpy as np
import torch
import argparse
import logging
import torch.nn as nn
import torch.backends.cudnn as cudnn
import torch.optim as optim
import torch.utils.data
import torchvision.utils as vutils

from common.data_loader import import_dataset
from common.tensorboard_logger import TensorboardLogger

import pandas as pd
from glob import glob

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from glob import glob
from PIL import Image


# load csv's
# dataload images w/ transforms
# import inception
# freeze layers
# train
# evaluate input
# evaluate output


def main():
    lesion_type_dict = {
        'nv': 'Melanocytic nevi',
        'mel': 'Melanoma',
        'bkl': 'Benign keratosis-like lesions ',
        'bcc': 'Basal cell carcinoma',
        'akiec': 'Actinic keratoses',
        'vasc': 'Vascular lesions',
        'df': 'Dermatofibroma'
    }


    base_skin_dir = os.path.join('dataset', 'skin-cancer-mnist-ham10000')

    # Merge images from both folders into one dictionary
    imageid_path_dict = {os.path.splitext(os.path.basename(x))[0]: x
                         for x in glob(os.path.join(base_skin_dir, '*', '*.jpg'))}


    # Read in the csv of metadata
    tile_df = pd.read_csv(os.path.join(base_skin_dir, 'HAM10000_metadata.csv'))

    tile_df['path'] = tile_df['image_id'].map(imageid_path_dict.get)
    tile_df['cell_type'] = tile_df['dx'].map(lesion_type_dict.get)
    tile_df['cell_type_idx'] = pd.Categorical(tile_df['cell_type']).codes
    print(tile_df.sample(5))

    # use 20 as validation

    input_dims = (50, 50)
    input_shape = input_dims + (3,)
    tile_df['image'] = tile_df['path'].map(lambda x: np.asarray(Image.open(x).resize(input_dims)))


if __name__ == '__main__':
    main()
