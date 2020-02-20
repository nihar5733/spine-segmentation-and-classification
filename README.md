# spine segmentation and classification
 Enter path to your dataset in path.txt with following format:
 	path/to/training/dataset
 	path/to/test/dataset

 Include following lines in your code to get paths:
 	'''python
 	path = open("../path.txt","r")
	p = path.readlines()
	trainDataPath = p[0]
	testDataPath = p[1]
	path.close()
	'''