import sys
import os
import csv
import numpy as np
import skimage


def loadData(dataPath):
	paths = [dataPath+"/Normal", dataPath+"/Damaged"]
	pathsAp = ["AP/Ap_Vertebra", "AP/Ap_Pedicle", "AP/Ap_Spinous_Process"]
	pathsLat = ["LAT/Lat_Vertebra", "LAT/Lat_Disk_Height", "LAT/Lat_Spinous_Process", "LAT/Lat_Anterior_Vertebral_Line", "LAT/Lat_Posterior_Vertebral_Line"]
	
	dataX = []; dataY= []

	for i in range(len(paths)):
		for d in os.listdir(paths[i]):
			t=[]
			for ap in pathsAp:
				t.append(skimage.io.imread(paths[i]+"/"+d+"/"+ap+".png"))
			for lat in pathsLat:
				t.append(skimage.io.imread(paths[i]+"/"+d+"/"+lat+".png"))
			dataX.append(t)
			dataY.append(i)

	return dataX, dataY


path = open("../path.txt","r")
p = path.readlines()
trainDataPath = p[0]
testDataPath = p[1]
path.close()

dataPath = "E:/IITD offline/ELL888/Assignment 1/Training"
dataX, dataY = loadData(dataPath)
print(len(dataX))
print((dataY))
