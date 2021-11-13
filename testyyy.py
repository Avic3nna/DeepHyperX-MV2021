from utils import open_file
import spectral
import os
import imageio

print(os.getcwd())
img = spectral.open_image('DeepHyperx\Datasets\WATER_HSI\REFLECTANCE_2021-09-12_003.hdr')

arr = img.load()
print(arr.shape)


lab = open_file('DeepHyperx\Datasets\WATER_HSI\labels.tiff')
print(lab.shape)

print(lab[1][1])

# img = open_file('.\\Datasets\\WATER_HSI\\results\\REFLECTANCE_2021-09-12_003.hdr')

# labels = open_file('.\\Datasets\\WATER_HSI\\labels.tiff')