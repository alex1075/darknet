import os
import glob

# file = open("/darknet/data/train/train.txt", "w")
# dirs = os.listdir("/darknet/data/train/")


def train_prep(file="/darknet/data/train/train.txt", dir="/darknet/data/train/"):
    filoo = open(file, 'w')
    for image in os.listdir(dir):
        if image.endswith(".jpg"):
            print(image)
            filoo.write("/darknet/data/train/" + image + "\n")
    filoo.close()

def test_prep(file="/darknet/data/test/test.txt", dir="/darknet/data/test/"):
    filoo = open(file, 'w')
    for image in os.listdir(dir):
        if image.endswith(".jpg"):
            print(image)
            filoo.write("/darknet/data/test/" + image + "\n")
    filoo.close()

def val_prep(file="/darknet/data/valid/valid.txt", dir="/darknet/data/valid/"):
    filoo = open(file, 'w')
    for image in os.listdir(dir):
        if image.endswith(".jpg"):
            print(image)
            filoo.write("/darknet/data/valid/" + image + "\n")
    filoo.close()

def allDaPrep():
    train_prep()
    test_prep()
    val_prep()

if __name__ == "__main__":
    allDaPrep()