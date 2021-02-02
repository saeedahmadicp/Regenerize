# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 22:06:57 2020

@author: Saeed Ahmad
"""

import tensorflow as tf
from keras.preprocessing.image import img_to_array, load_img
from skimage.transform import resize
from skimage.io import imsave
import numpy as np
from skimage.color import rgb2lab, lab2rgb, gray2rgb
from keras.applications.vgg16 import VGG16
from keras.models import Sequential

def colorize_image(sourceImg, img_type = "human"):
   
    
    if(img_type == "Nature Landscape"):

        #now we have one channel of L in each layer but, VGG16 is expecting 3 dimension, 
        #so we repeated the L channel two times to get 3 dimensions of the same L channel
        
        vggmodel = VGG16()
        newmodel = Sequential() 
        #num = 0
        '''here, we iterate on each layer except the last dense layers so, 
        we add 19 layer to our model. the dimension of last layer volume is “7x7x512”.
        '''
        for i, layer in enumerate(vggmodel.layers):
            if i<19:          #Only up to 19th layer to include feature extraction only
              newmodel.add(layer)
        
        
        
        
        #now we have one channel of L in each layer but, VGG16 is expecting 3 dimension, 
        #so we repeated the L channel two times to get 3 dimensions of the same L channel
        
        
        
        #Predicting and using saved model.
        model = tf.keras.models.load_model('other_files/colorize_autoencoder_nature_landscape.model',
                                           custom_objects=None,
                                           compile=True)
        #loading image from the path images/colorized/testimage directory
        testpath = sourceImg
        '''
        Python method listdir() returns a list containing the names of the entries in the directory given by path. 
        The list is in arbitrary order. It does not include the special entries '.' and '..'
        even if they are present in the directory.
        '''
            #converting the image into an array at the specified destination
        test = img_to_array(load_img(testpath))
        #converting it into 224 by 224 square image
        test = resize(test, (224,224), anti_aliasing=True)
        #Converting image from RGB color space to LAB color space and split the channels.
        test*= 1.0/255
        lab = rgb2lab(test)
        l = lab[:,:,0]
        #Converting image from gray color space to RGB.
        #Grayscale images only have one channel...but we provided it with three in the above line
        L = gray2rgb(l)
        #reshaping it so it meets our requirements of 224*224
        L = L.reshape((1,224,224,3))
        #predicitng the image using our preserved model
        vggpred = newmodel.predict(L)
        ab = model.predict(vggpred)
        ab = ab*128
        cur = np.zeros((224, 224, 3))
        cur[:,:,0] = l
        cur[:,:,1:] = ab
        #saving our model to the existing repository(/images with the name of format: result0/result1/...resultn.
        imsave("images/result1.jpg", lab2rgb(cur))
        img = "images/result1.jpg"
        return img
                
        
        
    else: 
        model = tf.keras.models.load_model('other_files/colorize_autoencoder.model',
                                           custom_objects=None,
                                                  compile=True)        
    
        img1_color=[]
        
        img1=img_to_array(load_img(sourceImg))
        img1 = resize(img1 ,(256,256))
        img1_color.append(img1)
        
        img1_color = np.array(img1_color, dtype=float)
        img1_color = rgb2lab(1.0/255*img1_color)[:,:,:,0]
        img1_color = img1_color.reshape(img1_color.shape+(1,))
        
        output1 = model.predict(img1_color)
        output1 = output1*128
        
        result = np.zeros((256, 256, 3))
        result[:,:,0] = img1_color[0][:,:,0]
        result[:,:,1:] = output1[0]
        imsave("images/result.jpg", lab2rgb(result))
        img = "images/result.jpg"
        return img 