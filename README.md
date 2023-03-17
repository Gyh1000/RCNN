# RCNN
RCNN using SS+CNN+SVM. Code in tensorflow2.11
It is a RCNN realization for academic and study


buy the way, I use cifar-10 to train the CNN, if you want to download cifar-10, please go to kaggle.

usage:
change the file path in load_image for the object you want to detect.
change the file path in load_data for the training data for CNN.
you can crecate your own CNN model in CNN_generate.

step 1:
run CNN_generate to generate a CNN model

step 2:
run SVM_generate to generate the SVM classification

step 3:
run object_detection to detect whether there is an object in  the picture.


说实在的有点想用中文做readme，英语写起来真的麻烦。
大家用的时候就先生成CNN，然后生成SVM，然后再去检测图片。
我是拿cifar-10去训练卷积神经网络的，就是想看看这样以后能不能识别正常图片里面的forg之类的，CNN模型很简单，想实用的话可以改的复杂点。
这个代码写完的时候，说实在的挺激动的。
感觉自己从代码小白变成了稍微会点代码的人了。
最后说一声，
这个只用作学术交流和学习用途，不作商业用途。

还有其他问题可以咨询544456490@qq.com
这是我的邮箱
