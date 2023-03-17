import tensorflow as tf
from tensorflow import keras
from keras import models
from keras import layers
from parse import parse
import load_data
#generate the image classification model
#using convolution neural network


def CNN_generate():
    arg=parse()
    model=keras.Sequential()
    model.add(layers.Rescaling(1.0/255))
    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.Flatten())
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(10))

    return model

def CNN_train(train,label):
    # train,label=load_data.load_train()
    # train=tf.convert_to_tensor(train,dtype=tf.float32)
    # label=tf.convert_to_tensor(label,dtype=tf.float32)
    arg=parse()
    model_name=arg.CNN_model_name
    epoch=arg.epoch
    learning_rate=arg.learning_rate
    validation_split=arg.validation_split
    validation_frequence=arg.validation_frequence
    batch_size=arg.batch_size
    model=CNN_generate()
    model.compile(
        optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
        # loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=['accuracy'],
    )
    model.fit(train,label,epochs=epoch,batch_size=batch_size,validation_split=validation_split,validation_freq=validation_frequence)

    if arg.show_model:
        model.show_model()


    model.save("CNN_model/"+model_name)

def CNN_pretrain():
    train, label = load_data.load_train()
    CNN_train(train, label)


if __name__=='__main__':
    CNN_pretrain()