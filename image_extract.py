from image_location import image_location
from parse import parse
import skimage
import numpy as np
def image_extract(image):
    arg=parse()

    img=image

    candidates=image_location(img)
    sub_image=[]
    for x,y,w,h in candidates:
        temp=img[x-1:x-1+w,y-1:y-1+h,:]
        sub_image.append(temp)

    return candidates,sub_image


if __name__=='__main__':
    image_extract(skimage.data.astronaut())