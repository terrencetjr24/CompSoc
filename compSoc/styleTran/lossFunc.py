from keras.datasets import mnist
from keras.models import Model, model_from_json
from keras.layers import Input, Conv2D, MaxPooling2D, UpSampling2D, Reshape
import numpy as np
#Each layer of the input layer and noise layer has a corresponding convolution vector
# I'm finding the difference vector, then taking the dot product of that with itself
# and returning that as the loss for that single layer

#Assumptions:
# 1. That after every convloution the data structure is represented as a vector
# 2. 

def loss_function(original_input, noise):
    holder = original_input - noise
        return (np.dot(holder,holder))


input_image = ----
input_style = ----
noise = np.random.rand()

image_loss = 0
style_loss = 0
        image_in = Input(shape=image_train.shape[1:])
        image_c1 = Conv2D(16, (3,3), activation='relu', padding='same')(image_in)
        image_p1 = MaxPooling2D((2,2), padding='same')(image_c1)
        noise_in = Input(shape=noise_train.shape[1:])
        noise_c1 = Conv2D(16, (3,3), activation='relu', padding='same')(noise_in)
        noise_p1 = MaxPooling2D((2,2), padding='same')(noise_c1)
        style_in = Input(shape=style_train.shape[1:])
        style_c1 = Conv2D(16, (3,3), activation='relu', padding='same')(style_in)
        style_p1 = MaxPooling2D((2,2), padding='same')(style_c1)
image_loss += loss_function(image_c1, noise_c1)
style_loss += loss_function(style_c1, noise_c1)

#And continuosly done for every layer in the network
