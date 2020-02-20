# Spine Segmentation and Classification
 Enter path to your dataset in path.txt with following format:
> path/to/training/dataset
> path/to/test/dataset

 Include following lines in your code to get paths:
```
path = open("../path.txt","r")
p = path.readlines()
trainDataPath = p[0]
testDataPath = p[1]
path.close()
```