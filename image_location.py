# -*- coding: utf-8 -*-
from __future__ import (
    division,
    print_function,
)
from skimage import data
import skimage.data
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import selectivesearch
from parse import parse



def image_location(image):
    arg = parse()
    image_size=arg.image_size
    length=arg.image_number
    # loading astronaut image
    img = image

    # perform selective search
    img_lbl, regions = selectivesearch.selective_search(
        img, scale=500, sigma=0.9, min_size=10)

    candidates = set()
    for r in regions:
        # excluding same rectangle (with different segments)
        if r['rect'] in candidates:
            continue
        # excluding regions smaller than 2000 pixels
        if r['size'] < image_size:
        # if r['size'] < 50 && w!=0 && h!=0:
            continue
        # distorted rects
        x, y, w, h = r['rect']
        if r['size'] < image_size & w!=0 & h!=0:
         if w / h > 1.2 or h / w > 1.2:
            continue
        if len(candidates) > length-1:
            continue
        candidates.add(r['rect'])
    return candidates

    # draw rectangles on the original image
    # fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(6, 6))
    # ax.imshow(img)
    # for x, y, w, h in candidates:
    #     # print(x, y, w, h)
    #     rect = mpatches.Rectangle(
    #         (x, y), w, h, fill=False, edgecolor='red', linewidth=1)
    #     # print(rect)
    #     ax.add_patch(rect)
    # # print(len(candidates))
    # plt.show()

if __name__ == "__main__":
    image_location(skimage.data.astronaut())
