import pandas as pd
import glob
import cv2
import numpy as np

def number_corresponding_label():
    temp_label = ['frog', 'truck', 'deer', 'automobile', 'bird', 'horse', 'ship', 'cat', 'dog', 'airplane']
    return temp_label


def load_train():
    y = pd.read_csv('trainLabels.csv')
    train = []
    label=[]
    temp_label=number_corresponding_label()
    images = glob.glob('train/train/*.png')
    for img in images:
        # print(img)
        img_arr = cv2.imread(img)
        img_arr = cv2.resize(img_arr, (32, 32))
        train.append(list(img_arr))
        temp = img.replace("train/train\\", "")
        temp = temp.replace(".png", "")
        temp = int(temp)
        label.append(y['label'].iloc[temp - 1])

    label_temp = []
    for labels in label:
        label_temp.append(temp_label.index(labels))

    # train = np.array(train, dtype=np.float32)
    # label = np.array(label_temp, dtype=np.float32)

    return train,label_temp






