import cv2
import glob


def load_image():
#return the required detected picture
#ndarray form
    data=[]
    images = glob.glob('*.jpg')
    for img in images:
        img_arr = cv2.imread(img)
        img_arr = cv2.resize(img_arr, (1000,1000))
        data.append(img_arr)
    # img_arr = cv2.resize(img_arr, (32, 32))
    return img_arr
