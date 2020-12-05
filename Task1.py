import os
import cv2
import pickle
import numpy
import pylab as plt


def GetAllImges(p, s):
    subfoldersNames = os.listdir(p)
    subfoldersNames.sort()
    imgsTest = []
    categoriesTest = []
    imgsTrain = []
    categoriesTrain = []
    for folderName in subfoldersNames:
        imageNames = os.listdir(path + "\\" + folderName)
        imageNames.sort()
        index = 0
        for imgName in imageNames:
            img = cv2.imread(path + "\\" + folderName + "\\" + imgName)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img = cv2.resize(img, (s, s))

            if len(imageNames) >= 50:
                if index < 25:
                    imgsTrain.append(img)
                    categoriesTrain.append(folderName)
                    index = index + 1
                else:
                    if index < 50:
                        imgsTest.append(img)
                        categoriesTest.append(folderName)
                        index = index + 1
                    else:
                        break
            else:
                if index < len(imageNames)/2:
                    imgsTrain.append(img)
                    categoriesTrain .append(folderName)
                    index = index + 1
                else:
                    imgsTest.append(img)
                    categoriesTest.append(folderName)
    return imgsTest, categoriesTest, imgsTrain, categoriesTrain

path = "C:\\Users\\sapir\\Downloads\\101_ObjectCategories\\101_ObjectCategories\\101_ObjectCategories"

def createImgFiles():
    imgsTest, categoriesTest, imgsTrain, categoriesTrain = GetAllImges(path, 300)
    with open('imgsTest.pkl', 'wb') as f:
        pickle.dump(imgsTest, f)
    with open('categoriesTest.pkl', 'wb') as f:
        pickle.dump(categoriesTest, f)
    with open('imgsTrain.pkl', 'wb') as f:
        pickle.dump(imgsTrain, f)
    with open('categoriesTrain.pkl', 'wb') as f:
        pickle.dump(categoriesTrain, f)

createImgFiles()
imgsTest, categoriesTest, imgsTrain, categoriesTrain = None, None, None, None
with open('imgsTest.pkl', 'wb') as f:
    pickle.dump(imgsTest, f)
with open('categoriesTest.pkl', 'wb') as f:
    pickle.dump(categoriesTest, f)
with open('imgsTrain.pkl', 'wb') as f:
    pickle.dump(imgsTrain, f)
with open('categoriesTrain.pkl', 'wb') as f:
    pickle.dump(categoriesTrain, f)

