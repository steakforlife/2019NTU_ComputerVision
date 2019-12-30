#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import math


# In[13]:


def laplacian1(image,threshold):
    laplcianOutput=np.zeros(shape=image.shape,dtype=image.dtype)
    output=np.zeros(shape=image.shape,dtype=image.dtype)
    imagePad=np.pad(image,((1,1),(1,1)),'reflect')
    rows,cols=image.shape
    for i in range(1,513):
        for j in range(1,513):
            graident=int(imagePad[i,j]*-4)+int(imagePad[i-1,j])+int(imagePad[i+1,j])+int(imagePad[i,j+1])+int(imagePad[i,j-1])
            if(graident>=threshold):
                laplcianOutput[i-1,j-1]=1
            elif(graident<=threshold*-1):
                laplcianOutput[i-1,j-1]=-1
            else:
                laplcianOutput[i-1,j-1]=0
    zeroCrossing=np.pad(laplcianOutput,((1,1),(1,1)),'reflect')
    for i in range(1,513):
        for j in range(1,513):
            if(zeroCrossing[i,j]==1):
                if([zeroCrossing[i-1,j-1],zeroCrossing[i-1,j],zeroCrossing[i-1,j+1],                   zeroCrossing[i,j-1],zeroCrossing[i,j],zeroCrossing[i,j+1],                   zeroCrossing[i+1,j-1],zeroCrossing[i+1,j],zeroCrossing[i+1,j+1]].count(-1)>0):
                    output[i-1,j-1]=0
            else:
                output[i-1,j-1]=255
    return output


# In[14]:


#test
src=cv2.imread("lena.bmp",0)
test=laplacian1(src,15)
cv2.imwrite("laplacian1.bmp",test)


# In[15]:


def laplacian2(image,threshold):
    laplcianOutput=np.zeros(shape=image.shape,dtype=image.dtype)
    output=np.zeros(shape=image.shape,dtype=image.dtype)
    imagePad=np.pad(image,((1,1),(1,1)),'reflect')
    rows,cols=image.shape
    for i in range(1,513):
        for j in range(1,513):
            graident=int(imagePad[i,j]*-8)+int(imagePad[i-1,j])+int(imagePad[i+1,j])+int(imagePad[i,j+1])+int(imagePad[i,j-1])                    +int(imagePad[i-1,j-1])+int(imagePad[i-1,j+1])+int(imagePad[i+1,j-1])+int(imagePad[i+1,j+1])
            graident=int(graident/3)
            
            if(graident>=threshold):
                laplcianOutput[i-1,j-1]=1
            elif(graident<=threshold*-1):
                laplcianOutput[i-1,j-1]=-1
            else:
                laplcianOutput[i-1,j-1]=0
    zeroCrossing=np.pad(laplcianOutput,((1,1),(1,1)),'reflect')
    for i in range(1,513):
        for j in range(1,513):
            if(zeroCrossing[i,j]==1):
                if([zeroCrossing[i-1,j-1],zeroCrossing[i-1,j],zeroCrossing[i-1,j+1],                   zeroCrossing[i,j-1],zeroCrossing[i,j],zeroCrossing[i,j+1],                   zeroCrossing[i+1,j-1],zeroCrossing[i+1,j],zeroCrossing[i+1,j+1]].count(-1)>0):
                    output[i-1,j-1]=0
            else:
                output[i-1,j-1]=255
    return output


# In[16]:


#test
src=cv2.imread("lena.bmp",0)
test=laplacian2(src,15)
cv2.imwrite("laplacian2.bmp",test)


# In[17]:


def minVarLaplacian(image,threshold):
    laplcianOutput=np.zeros(shape=image.shape,dtype=image.dtype)
    output=np.zeros(shape=image.shape,dtype=image.dtype)
    imagePad=np.pad(image,((1,1),(1,1)),'reflect')
    rows,cols=image.shape
    for i in range(1,513):
        for j in range(1,513):
            graident=int(imagePad[i,j]*-4)+int(imagePad[i-1,j]*-1)+int(imagePad[i+1,j]*-1)+int(imagePad[i,j+1]*-1)+int(imagePad[i,j-1]*-1)                    +int(imagePad[i-1,j-1]*2)+int(imagePad[i-1,j+1]*2)+int(imagePad[i+1,j-1]*2)+int(imagePad[i+1,j+1]*2)
            graident=int(graident/3)
            
            if(graident>=threshold):
                laplcianOutput[i-1,j-1]=1
            elif(graident<=threshold*-1):
                laplcianOutput[i-1,j-1]=-1
            else:
                laplcianOutput[i-1,j-1]=0
    zeroCrossing=np.pad(laplcianOutput,((1,1),(1,1)),'reflect')
    for i in range(1,513):
        for j in range(1,513):
            if(zeroCrossing[i,j]==1):
                if([zeroCrossing[i-1,j-1],zeroCrossing[i-1,j],zeroCrossing[i-1,j+1],                   zeroCrossing[i,j-1],zeroCrossing[i,j],zeroCrossing[i,j+1],                   zeroCrossing[i+1,j-1],zeroCrossing[i+1,j],zeroCrossing[i+1,j+1]].count(-1)>0):
                    output[i-1,j-1]=0
            else:
                output[i-1,j-1]=255
    return output


# In[18]:


#test
src=cv2.imread("lena.bmp",0)
test=minVarLaplacian(src,20)
cv2.imwrite("minVarLaplcian.bmp",test)


# In[23]:


def laplcianOfGaussian(image,threshold):
    laplcianOutput=np.zeros(shape=image.shape,dtype=image.dtype)
    output=np.zeros(shape=image.shape,dtype=image.dtype)
    imagePad=np.pad(image,((5,5),(5,5)),'reflect')
    rows,cols=image.shape
    for i in range(5,517):
        for j in range(5,517):
            graident=int(imagePad[i,j]*178)+int(imagePad[i-1,j]*103)+int(imagePad[i+1,j]*103)+int(imagePad[i,j+1]*103)+int(imagePad[i,j-1]*103)                    +int(imagePad[i-1,j-1]*52)+int(imagePad[i-1,j+1]*52)+int(imagePad[i+1,j-1]*52)+int(imagePad[i+1,j+1]*52                    +int(imagePad[i+2,j]*-1)+int(imagePad[i-2,j]*-1)+int(imagePad[i,j+2]*-1)+int(imagePad[i,j-2]*-1)                    +int(imagePad[i+1,j-2]*-14)+int(imagePad[i+1,j+2]*-14)+int(imagePad[i-1,j-2]*-14)+int(imagePad[i-1,j+2]*-14)                    +int(imagePad[i+2,j-1]*-14)+int(imagePad[i+2,j+1]*-14)+int(imagePad[i-2,j-1]*-14)+int(imagePad[i-2,j+1]*-14)                    +int(imagePad[i+2,j+2]*-24)+int(imagePad[i+2,j-2]*-24)+int(imagePad[i-2,j+2]*-24)+int(imagePad[i-2,j-2]*-24)                    +int(imagePad[i+3,j]*-23)+int(imagePad[i-3,j]*-23)+int(imagePad[i,j+3]*-23)+int(imagePad[i,j-3]*-23)                    +int(imagePad[i+3,j+1]*-22)+int(imagePad[i+3,j-1]*-22)+int(imagePad[i-3,j+1]*-22)+int(imagePad[i-3,j-1]*-22)                    +int(imagePad[i+1,j+3]*-22)+int(imagePad[i+1,j-3]*-22)+int(imagePad[i-1,j+3]*-22)+int(imagePad[i-1,j-3]*-22)                    +int(imagePad[i+3,j+2]*-15)+int(imagePad[i+3,j-2]*-15)+int(imagePad[i-3,j+2]*-15)+int(imagePad[i-3,j-2]*-15)                    +int(imagePad[i+2,j+3]*-15)+int(imagePad[i+2,j-3]*-15)+int(imagePad[i-2,j+3]*-15)+int(imagePad[i-2,j-3]*-15)                    +int(imagePad[i+3,j+3]*-7)+int(imagePad[i+3,j-3]*-7)+int(imagePad[i-3,j+3]*-7)+int(imagePad[i-3,j-3]*-7)                    +int(imagePad[i+4,j]*-9)+int(imagePad[i-4,j]*-9)+int(imagePad[i,j+4]*-9)+int(imagePad[i,j-4]*-9)                    +int(imagePad[i+4,j+1]*-8)+int(imagePad[i-4,j-1]*-8)+int(imagePad[i+1,j+4]*-8)+int(imagePad[i-1,j-4]*-8)                    +int(imagePad[i-4,j+1]*-8)+int(imagePad[i+4,j-1]*-8)+int(imagePad[i+1,j-4]*-8)+int(imagePad[i-1,j+4]*-8)                    +int(imagePad[i+4,j+2]*-4)+int(imagePad[i-4,j-2]*-4)+int(imagePad[i+2,j+4]*-4)+int(imagePad[i-2,j-4]*-4)                    +int(imagePad[i-4,j+2]*-4)+int(imagePad[i+4,j-2]*-4)+int(imagePad[i+2,j-4]*-4)+int(imagePad[i-2,j+4]*-4)                    +int(imagePad[i+4,j+3]*-2)+int(imagePad[i-4,j-3]*-2)+int(imagePad[i+3,j+4]*-2)+int(imagePad[i-3,j-4]*-2)                    +int(imagePad[i-4,j+3]*-2)+int(imagePad[i+4,j-3]*-2)+int(imagePad[i+3,j-4]*-2)+int(imagePad[i-3,j+4]*-2)                    +int(imagePad[i+5,j]*-2)+int(imagePad[i-5,j]*-2)+int(imagePad[i,j+5]*-2)+int(imagePad[i,j-5]*-2)                    +int(imagePad[i+5,j+1]*-1)+int(imagePad[i-5,j-1]*-1)+int(imagePad[i+1,j+5]*-1)+int(imagePad[i-1,j-5]*-1)                    +int(imagePad[i-5,j+1]*-1)+int(imagePad[i+5,j-1]*-1)+int(imagePad[i+1,j-5]*-1)+int(imagePad[i-1,j+5]*-1)                    +int(imagePad[i+5,j+2]*-1)+int(imagePad[i-5,j-2]*-1)+int(imagePad[i+2,j+5]*-1)+int(imagePad[i-2,j-5]*-1)                    +int(imagePad[i-5,j+2]*-1)+int(imagePad[i+5,j-2]*-1)+int(imagePad[i+2,j-5]*-1)+int(imagePad[i-2,j+5]*-1))
            
            
            if(graident>=threshold):
                laplcianOutput[i-5,j-5]=1
            elif(graident<=threshold*-1):
                laplcianOutput[i-5,j-5]=-1
            else:
                laplcianOutput[i-5,j-5]=0
    zeroCrossing=np.pad(laplcianOutput,((1,1),(1,1)),'reflect')
    for i in range(1,513):
        for j in range(1,513):
            if(zeroCrossing[i,j]==1):
                if([zeroCrossing[i-1,j-1],zeroCrossing[i-1,j],zeroCrossing[i-1,j+1],                   zeroCrossing[i,j-1],zeroCrossing[i,j],zeroCrossing[i,j+1],                   zeroCrossing[i+1,j-1],zeroCrossing[i+1,j],zeroCrossing[i+1,j+1]].count(-1)>0):
                    output[i-1,j-1]=0
            else:
                output[i-1,j-1]=255
    return output


# In[25]:


#test
src=cv2.imread("lena.bmp",0)
test=laplcianOfGaussian(src,3000)
cv2.imwrite("laplcianOfGaussian.bmp",test)


# In[34]:


def differenceOfGaussian(image,threshold):
    laplcianOutput=np.zeros(shape=image.shape,dtype=image.dtype)
    output=np.zeros(shape=image.shape,dtype=image.dtype)
    imagePad=np.pad(image,((5,5),(5,5)),'reflect')
    rows,cols=image.shape
    for i in range(5,517):
        for j in range(5,517):
            graident=int(imagePad[i,j]*283)+int(imagePad[i-1,j]*160)+int(imagePad[i+1,j]*160)+int(imagePad[i,j+1]*160)+int(imagePad[i,j-1]*160)                    +int(imagePad[i-1,j-1]*85)+int(imagePad[i-1,j+1]*85)+int(imagePad[i+1,j-1]*85)+int(imagePad[i+1,j+1]*85                    +int(imagePad[i+2,j]*15)+int(imagePad[i-2,j]*15)+int(imagePad[i,j+2]*15)+int(imagePad[i,j-2]*15)                    +int(imagePad[i+2,j+2]*-16)+int(imagePad[i+2,j-2]*-16)+int(imagePad[i-2,j+2]*-16)+int(imagePad[i-2,j-2]*-16)                    +int(imagePad[i+3,j]*-17)+int(imagePad[i-3,j]*-17)+int(imagePad[i,j+3]*-17)+int(imagePad[i,j-3]*-17)                    +int(imagePad[i+3,j+1]*-17)+int(imagePad[i+3,j-1]*-17)+int(imagePad[i-3,j+1]*-17)+int(imagePad[i-3,j-1]*-17)                    +int(imagePad[i+1,j+3]*-17)+int(imagePad[i+1,j-3]*-17)+int(imagePad[i-1,j+3]*-17)+int(imagePad[i-1,j-3]*-17)
                    +int(imagePad[i+3,j+2]*-16)+int(imagePad[i+3,j-2]*-16)+int(imagePad[i-3,j+2]*-16)+int(imagePad[i-3,j-2]*-16)\
                    +int(imagePad[i+2,j+3]*-16)+int(imagePad[i+2,j-3]*-16)+int(imagePad[i-2,j+3]*-16)+int(imagePad[i-2,j-3]*-16)\
                    +int(imagePad[i+3,j+3]*-12)+int(imagePad[i+3,j-3]*-12)+int(imagePad[i-3,j+3]*-12)+int(imagePad[i-3,j-3]*-12)\
                    +int(imagePad[i+4,j]*-13)+int(imagePad[i-4,j]*-13)+int(imagePad[i,j+4]*-13)+int(imagePad[i,j-4]*-13)\
                    +int(imagePad[i+4,j+1]*-13)+int(imagePad[i-4,j-1]*-13)+int(imagePad[i+1,j+4]*-13)+int(imagePad[i-1,j-4]*-13)\
                    +int(imagePad[i-4,j+1]*-13)+int(imagePad[i+4,j-1]*-13)+int(imagePad[i+1,j-4]*-13)+int(imagePad[i-1,j+4]*-13)\
                    +int(imagePad[i+4,j+2]*-11)+int(imagePad[i-4,j-2]*-11)+int(imagePad[i+2,j+4]*-11)+int(imagePad[i-2,j-4]*-11)\
                    +int(imagePad[i-4,j+2]*-11)+int(imagePad[i+4,j-2]*-11)+int(imagePad[i+2,j-4]*-11)+int(imagePad[i-2,j+4]*-11)\
                    +int(imagePad[i+4,j+3]*-8)+int(imagePad[i-4,j-3]*-8)+int(imagePad[i+3,j+4]*-8)+int(imagePad[i-3,j-4]*-8)\
                    +int(imagePad[i-4,j+3]*-8)+int(imagePad[i+4,j-3]*-8)+int(imagePad[i+3,j-4]*-8)+int(imagePad[i-3,j+4]*-8)\
                    +int(imagePad[i+4,j+4]*-5)+int(imagePad[i-4,j-4]*-5)+int(imagePad[i+4,j+4]*-5)+int(imagePad[i-4,j-4]*-5)\
                    +int(imagePad[i+5,j]*-8)+int(imagePad[i-5,j]*-8)+int(imagePad[i,j+5]*-8)+int(imagePad[i,j-5]*-8)\
                    +int(imagePad[i+5,j+1]*-7)+int(imagePad[i-5,j-1]*-7)+int(imagePad[i+1,j+5]*-7)+int(imagePad[i-1,j-5]*-7)\
                    +int(imagePad[i-5,j+1]*-7)+int(imagePad[i+5,j-1]*-7)+int(imagePad[i+1,j-5]*-7)+int(imagePad[i-1,j+5]*-7)\
                    +int(imagePad[i+5,j+2]*-6)+int(imagePad[i-5,j-2]*-6)+int(imagePad[i+2,j+5]*-6)+int(imagePad[i-2,j-5]*-6)\
                    +int(imagePad[i-5,j+2]*-6)+int(imagePad[i+5,j-2]*-6)+int(imagePad[i+2,j-5]*-6)+int(imagePad[i-2,j+5]*-6)\
                    +int(imagePad[i+5,j+3]*-4)+int(imagePad[i-5,j-3]*-4)+int(imagePad[i+3,j+5]*-4)+int(imagePad[i-3,j-5]*-4)\
                    +int(imagePad[i-5,j+3]*-4)+int(imagePad[i+5,j-3]*-4)+int(imagePad[i+3,j-5]*-4)+int(imagePad[i-3,j+5]*-4)\
                    +int(imagePad[i+5,j+4]*-3)+int(imagePad[i-5,j-4]*-3)+int(imagePad[i+4,j+5]*-3)+int(imagePad[i-4,j-5]*-3)\
                    +int(imagePad[i-5,j+4]*-3)+int(imagePad[i+5,j-4]*-3)+int(imagePad[i+4,j-5]*-3)+int(imagePad[i-4,j+5]*-3)\
                    +int(imagePad[i+5,j+5]*-1)+int(imagePad[i-5,j-5]*-1)+int(imagePad[i+5,j+5]*-1)+int(imagePad[i-5,j-5]*-1))
            
            
            if(graident>=threshold):
                laplcianOutput[i-5,j-5]=1
            elif(graident<=threshold*-1):
                laplcianOutput[i-5,j-5]=-1
            else:
                laplcianOutput[i-5,j-5]=0
    zeroCrossing=np.pad(laplcianOutput,((1,1),(1,1)),'reflect')
    for i in range(1,513):
        for j in range(1,513):
            if(zeroCrossing[i,j]==1):
                if([zeroCrossing[i-1,j-1],zeroCrossing[i-1,j],zeroCrossing[i-1,j+1],                   zeroCrossing[i,j-1],zeroCrossing[i,j],zeroCrossing[i,j+1],                   zeroCrossing[i+1,j-1],zeroCrossing[i+1,j],zeroCrossing[i+1,j+1]].count(-1)>0):
                    output[i-1,j-1]=0
            else:
                output[i-1,j-1]=255
    for i in range(rows):
        for j in range(cols):
            if(output[i,j]==255):
                output[i,j]=0
            else:
                output[i,j]=255
    return output


# In[36]:


#test
src=cv2.imread("lena.bmp",0)
test=differenceOfGaussian(src,1)
cv2.imwrite("differenceOfGaussian.bmp",test)


# In[ ]:




