from utils import open_file
import numpy as np
import os

CUSTOM_DATASETS_CONFIG = {
    "DFC2018_HSI": {
        "img": "2018_IEEE_GRSS_DFC_HSI_TR.HDR",
        "gt": "2018_IEEE_GRSS_DFC_GT_TR.tif",
        "download": False,
        "loader": lambda folder: dfc2018_loader(folder),
    },
    "WATER_HSI": {
        "img": "hsi_water_train.mat",
        "gt": "hsi_water_train_gt.tiff",
        "download": False,
        "loader": lambda folder: water_loader(folder),
    },
    "SNOW_HSI": {
        "img": "hsi_snow_train.mat",
        "gt": "hsi_snow_train_gt.tiff",
        "download": False,
        "loader": lambda folder: snow_loader(folder),
    }
}


def dfc2018_loader(folder):
    img = open_file(folder + "2018_IEEE_GRSS_DFC_HSI_TR.HDR")[:, :, :-2]
    gt = open_file(folder + "2018_IEEE_GRSS_DFC_GT_TR.tif")
    gt = gt.astype("uint8")

    rgb_bands = (5, 10, 25)

    label_values = [
        "Unclassified",
        "Healthy grass",
        "Stressed grass",
        "Artificial turf",
        "Evergreen trees",
        "Deciduous trees",
        "Bare earth",
        "Water",
        "Residential buildings",
        "Non-residential buildings",
        "Roads",
        "Sidewalks",
        "Crosswalks",
        "Major thoroughfares",
        "Highways",
        "Railways",
        "Paved parking lots",
        "Unpaved parking lots",
        "Cars",
        "Trains",
        "Stadium seats",
    ]
    ignored_labels = [0]
    palette = None
    return img, gt, rgb_bands, ignored_labels, label_values, palette

# undefined, rocks, gravel and dirt ignored
def water_loader(folder):
    img = open_file(folder + "hsi_water_train.mat")
    gt = open_file(folder + "hsi_water_train_gt.tiff")
    gt = gt.astype("uint8")

    rgb_bands = (10, 15, 25)

    label_values = [
        "undefined",
        "Grass",
        "Concrete",
        "Asphalt",
        "Trees",
        "Rocks",
        "Water",
        "Sky",
        "Gravel",
        "Object",
        "Dirt",
        "Mud",
    ]
    ignored_labels = [0,5,8,10]
    palette = None
    return img, gt, rgb_bands, ignored_labels, label_values, palette

def snow_loader(folder):
    img = open_file(folder + "hsi_snow_train.mat")
    gt = open_file(folder + "hsi_snow_train_gt.tiff")
    gt = gt.astype("uint8")

    rgb_bands = (10, 15, 25)

    label_values = [
        "undefined",
        "Grass",
        "Concrete",
        "Asphalt",
        "Trees",
        "Rocks",
        "Water",
        "Sky",
        "Gravel",
        "Object",
        "Dirt",
        "Mud",
        "Snow",
        "Ice",
    ]
    ignored_labels = [0,5,8,10]
    palette = None
    return img, gt, rgb_bands, ignored_labels, label_values, palette
