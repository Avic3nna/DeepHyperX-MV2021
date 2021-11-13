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
        "img": "REFLECTANCE_2021-09-12_003.hdr",
        "gt": "labels.tiff",
        "download": False,
        "loader": lambda folder: water_loader(folder),
    }
}


def dfc2018_loader(folder):
    img = open_file(folder + "2018_IEEE_GRSS_DFC_HSI_TR.HDR")[:, :, :-2]
    gt = open_file(folder + "2018_IEEE_GRSS_DFC_GT_TR.tif")
    gt = gt.astype("uint8")

    rgb_bands = (47, 31, 15)

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

def water_loader(folder):
    img = open_file(folder + "REFLECTANCE_2021-09-12_003.hdr")
    gt = open_file(folder + "label003.tiff")
    gt = gt.astype("uint8")

    rgb_bands = (47, 31, 15)

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
    ignored_labels = [0]
    palette = None
    return img, gt, rgb_bands, ignored_labels, label_values, palette
