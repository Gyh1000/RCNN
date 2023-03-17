import numpy as np

from image_extract import image_extract
from load_image import load_image
import tensorflow as tf
from tensorflow import keras
from keras import models
from SVM import SVM
from parse import parse
import SVM_generate
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import process_prediction
import load_data

def object_detection():
    arg=parse()
    image=load_image()
    model_name=arg.CNN_model_name
    model=models.load_model("CNN_model/"+model_name)
    clf=SVM_generate.load_generated_SVM_modal()
    label=load_data.number_corresponding_label()
    # finall_prediction=[]
    for img in image:
        finall_prediction = []
        candidates,sub_image=image_extract(img)
        sub_image=np.array(sub_image,dtype=np.float32)
        sub_image=tf.convert_to_tensor(sub_image,dtype=tf.float32)
        intermediate_variable=model.predict(sub_image)  #50*10
        for svm in clf:
            prediction=svm.predict(intermediate_variable)   #50*1
            finall_prediction.append(prediction)            #10*50*1
        #对预测结果进行滤波
        #滤波返回标签和位置（label+candidates）
        #finall_prediction应该是10*50维数组
        record,result=process_prediction.process_prediction(finall_prediction)
        array=np.array(candidates,dtype=np.float32)
        array2=np.array(result,dtype=np.float)
        candidates_left=np.delete(array,record,axis=0)
        result_left=np.delete(array2,record,axis=0)

        #result_left记录了不同类别的概率信息
        #candidates_left记录了剩下的方块

        #result_left保留2位小数,且变成百分数
        result_left=result_left*100
        result_left=np.around(result_left,decimals=2)
        #现在已经有了预测结果，开始画图
        # draw rectangles on the original image
        fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(6, 6))
        ax.imshow(img)
        j=0
        for x, y, w, h in candidates_left:
            # print(x, y, w, h)
            rect = mpatches.Rectangle(
                (x, y), w, h, fill=False, edgecolor='red', linewidth=1)
            # print(rect)
            ax.add_patch(rect)
            for i in range(10):
                text=plt.text(x, y+i, label[i]+":"+str(result_left[j,i]+"%"), ha='left', wrap=True)
                ax.add_patch(text)
            j+=1
        # print(len(candidates))
        plt.show()



if __name__=='__main__':
    object_detection()
