import sys
import os
import csv
import cv2
import numpy as np
from skimage import io as io
from skimage.transform import rescale, resize, downscale_local_mean
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical

def loadData(dataPath):
    paths = [dataPath + "/Normal", dataPath + "/Damaged"]
    masks = ["AP/Ap_Vertebra", "LAT/Lat_Vertebra", "LAT/Lat_Disk_Height"]
    
    dataX = []
    dataY = []
    
    for i in range(len(paths)):
        for d in os.listdir(paths[i]):
            print(d)
            try:
                t = []
                for m in masks:
                    img = np.array(io.imread(paths[i] + "/" + d + "/" + m + ".png"))
                    rows = np.where(np.max(img,0) > 0)
                    cols = np.where(np.max(img,1) > 0)
                    cropped=img[cols[0][0]: cols[0][-1] + 1, rows[0][0]: rows[0][-1] + 1]
                    img_rs = cv2.resize(cropped, (132,360))

                    t.append(img_rs)

                dataX.append(t)
                dataY.append(i)
            except IOError:
                print("Skipping " + d)
    
    return dataX, dataY

# path = open("../path.txt", "r")
# p = path.readlines()
# trainDataPath = p[0]
# testDataPath = p[1]
# path.close()
dataPath = "/content/drive/My Drive/Colab Notebooks/spineDataSet/Training"
dataX, dataY = loadData(dataPath)
X = [np.array(x) for x in dataX]
X=np.array(X)
Y = np.array(dataY)

x_train, x_valid, y_train, y_valid = train_test_split(X, Y, test_size=0.3, shuffle= True)
x_train = np.transpose(x_train,(0,3,2,1))
y_train = to_categorical(y_train)
x_valid = np.transpose(x_valid,(0,3,2,1))
y_valid = to_categorical(y_valid)

