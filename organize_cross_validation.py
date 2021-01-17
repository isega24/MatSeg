import os
import numpy as np
import pandas as pd
from shutil import copyfile



## Obtain all the images

allFiles = ["./data/uhcs/train/images/"+elem for elem in os.listdir("./data/uhcs/train/images")] + ["data/uhcs/validate/images/" + elem for elem in os.listdir("data/uhcs/validate/images")]

cross_validation = pd.read_csv("uhcs_split.csv")

cross_validation_separation = np.array(cross_validation.values)
treeDirectory = "./data/uhcs-fold-"
for i in np.unique(cross_validation_separation[:,1]):
    print(f"{treeDirectory}{i}/")
    foldDirectory = f"{treeDirectory}{i}/"
    os.mkdir(foldDirectory)

    os.mkdir(foldDirectory+"train/")
    os.mkdir(foldDirectory+"train/images/")
    os.mkdir(foldDirectory+"train/labels/")
    os.mkdir(foldDirectory+"train/labels_npy/")

    os.mkdir(foldDirectory+"test/")
    os.mkdir(foldDirectory+"test/images/")
    os.mkdir(foldDirectory+"test/labels/")
    os.mkdir(foldDirectory+"test/labels_npy/")

    
    for elem in range(len(cross_validation_separation)):
        indexAllFiles = np.where([cross_validation_separation[elem,0] in allFiles[j] for j in range(len(cross_validation_separation)) ])[0][0]
        print(cross_validation_separation[elem,0] in allFiles[indexAllFiles])
        if cross_validation_separation[elem,1] == i:
            print("Este para test")
            copyfile(allFiles[indexAllFiles], foldDirectory+"test/images/"+allFiles[indexAllFiles].split("/")[-1])
            copyfile(allFiles[indexAllFiles].replace("images","labels"), foldDirectory+"test/labels/"+allFiles[indexAllFiles].split("/")[-1])
            copyfile(allFiles[indexAllFiles].replace("images","labels_npy").replace(".tif",".npy"), foldDirectory+"test/labels_npy/"+allFiles[indexAllFiles].split("/")[-1].replace(".tif",".npy"))
            
        else:
            print("Este para train")
            copyfile(allFiles[indexAllFiles], foldDirectory+"train/images/"+allFiles[indexAllFiles].split("/")[-1])
            copyfile(allFiles[indexAllFiles].replace("images","labels"), foldDirectory+"train/labels/"+allFiles[indexAllFiles].split("/")[-1])
            copyfile(allFiles[indexAllFiles].replace("images","labels_npy").replace(".tif",".npy"), foldDirectory+"train/labels_npy/"+allFiles[indexAllFiles].split("/")[-1].replace(".tif",".npy"))

            
            

