#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import math


# In[4]:


def robertOperator(image,threshold):
    output=np.zeros(shape=image.shape,dtype=image.dtype)
    imagePad=np.pad(image,((1,1),(1,1)),'reflect')
    rows,cols=image.shape
    for i in range(rows):
        for j in range(cols):
            r1=int(imagePad[i+2,j+2])-int(imagePad[i+1,j+1])
            r2=int(imagePad[i+1,j+2])-int(imagePad[i+2,j+1])
            graident=(math.sqrt(r1**2+r2**2))
            if(graident>threshold):
                output[i,j]=0
            else:
                output[i,j]=255
    return output


# In[34]:


#test
src=cv2.imread("lena.bmp",0)
test=robertOperator(src,12)
cv2.imwrite("robert.bmp",test)


# In[13]:


np.where(src>255)
srcPad=np.pad(src,((1,1),(1,1)),'reflect')
np.where(srcPad>255)
srcPad[2,4]


# In[43]:


for i in range(1,3):
    print(i)


# In[45]:


def prewittOperator(image,threshold):
    rows,cols=image.shape
    output=np.zeros(shape=image.shape)
    imagePad=np.pad(image,((1,1),(1,1)),'reflect')
    for i in range(1,513):
        for j in range(1,513):
            p1= int(imagePad[i-1,j+1])+int(imagePad[i,j+1])+int(imagePad[i+1,j+1])                -int(imagePad[i-1,j-1])-int(imagePad[i,j-1])-int(imagePad[i+1,j-1])
            p2= int(imagePad[i+1,j-1])+int(imagePad[i+1,j])+int(imagePad[i+1,j+1])                -int(imagePad[i-1,j-1])-int(imagePad[i-1,j])-int(imagePad[i+1,j])
            graident=(math.sqrt(p1**2+p2**2))
            if graident>threshold:
                output[i-1,j-1]=0
            else:
                output[i-1,j-1]=255
    return output


# In[46]:


#test
src=cv2.imread("lena.bmp",0)
test=prewittOperator(src,24)
cv2.imwrite("prewitt.bmp",test)


# In[47]:


def sobelOperator(image,threshold):
    rows,cols=image.shape
    output=np.zeros(shape=image.shape)
    imagePad=np.pad(image,((1,1),(1,1)),'reflect')
    for i in range(1,513):
        for j in range(1,513):
            p1= int(imagePad[i-1,j+1])+int(2*imagePad[i,j+1])+int(imagePad[i+1,j+1])                -int(imagePad[i-1,j-1])-int(2*imagePad[i,j-1])-int(imagePad[i+1,j-1])
            p2= int(imagePad[i+1,j-1])+int(2*imagePad[i+1,j])+int(imagePad[i+1,j+1])                -int(imagePad[i-1,j-1])-int(2*imagePad[i-1,j])-int(imagePad[i+1,j])
            graident=(math.sqrt(p1**2+p2**2))
            if graident>threshold:
                output[i-1,j-1]=0
            else:
                output[i-1,j-1]=255
    return output


# In[48]:


#test
src=cv2.imread("lena.bmp",0)
test=sobelOperator(src,38)
cv2.imwrite("sobel.bmp",test)


# In[49]:


def FreiandChenOperator(image,threshold):
    rows,cols=image.shape
    output=np.zeros(shape=image.shape)
    imagePad=np.pad(image,((1,1),(1,1)),'reflect')
    for i in range(1,513):
        for j in range(1,513):
            p1= int(imagePad[i-1,j+1])+int(math.sqrt(2)*imagePad[i,j+1])+int(imagePad[i+1,j+1])                -int(imagePad[i-1,j-1])-int(math.sqrt(2)*imagePad[i,j-1])-int(imagePad[i+1,j-1])
            p2= int(imagePad[i+1,j-1])+int(math.sqrt(2)*imagePad[i+1,j])+int(imagePad[i+1,j+1])                -int(imagePad[i-1,j-1])-int(math.sqrt(2)*imagePad[i-1,j])-int(imagePad[i+1,j])
            graident=(math.sqrt(p1**2+p2**2))
            if graident>threshold:
                output[i-1,j-1]=0
            else:
                output[i-1,j-1]=255
    return output


# In[50]:


#test
src=cv2.imread("lena.bmp",0)
test=FreiandChenOperator(src,30)
cv2.imwrite("freiandchen.bmp",test)


# In[51]:


def kirschCompassOperator(image,threshold):
    rows,cols=image.shape
    output=np.zeros(shape=image.shape)
    imagePad=np.pad(image,((1,1),(1,1)),'reflect')
    for i in range(1,513):
        for j in range(1,513):
            k=np.zeros(8)
            """
            1 2 6
            3   7
            4 5 8
            """
            k[0]=int(-3*imagePad[i-1,j-1])+int(-3*imagePad[i,j-1])+int(-3*imagePad[i-1,j])+int(-3*imagePad[i-1,j+1])                 +int(-3*imagePad[i,j+1])+int(5*imagePad[i+1,j-1])+int(5*imagePad[i+1,j])+int(5*imagePad[i+1,j+1])
            k[1]=int(-3*imagePad[i-1,j-1])+int(5*imagePad[i,j-1])+int(-3*imagePad[i-1,j])+int(-3*imagePad[i-1,j+1])                 +int(-3*imagePad[i,j+1])+int(5*imagePad[i+1,j-1])+int(5*imagePad[i+1,j])+int(-3*imagePad[i+1,j+1])
            k[2]=int(5*imagePad[i-1,j-1])+int(5*imagePad[i,j-1])+int(-3*imagePad[i-1,j])+int(-3*imagePad[i-1,j+1])                 +int(-3*imagePad[i,j+1])+int(5*imagePad[i+1,j-1])+int(-3*imagePad[i+1,j])+int(-3*imagePad[i+1,j+1])
            k[3]=int(5*imagePad[i-1,j-1])+int(5*imagePad[i,j-1])+int(5*imagePad[i-1,j])+int(-3*imagePad[i-1,j+1])                 +int(-3*imagePad[i,j+1])+int(-3*imagePad[i+1,j-1])+int(-3*imagePad[i+1,j])+int(-3*imagePad[i+1,j+1])
            k[4]=int(5*imagePad[i-1,j-1])+int(-3*imagePad[i,j-1])+int(5*imagePad[i-1,j])+int(5*imagePad[i-1,j+1])                 +int(-3*imagePad[i,j+1])+int(-3*imagePad[i+1,j-1])+int(-3*imagePad[i+1,j])+int(-3*imagePad[i+1,j+1])
            k[5]=int(-3*imagePad[i-1,j-1])+int(-3*imagePad[i,j-1])+int(5*imagePad[i-1,j])+int(5*imagePad[i-1,j+1])                 +int(5*imagePad[i,j+1])+int(-3*imagePad[i+1,j-1])+int(-3*imagePad[i+1,j])+int(-3*imagePad[i+1,j+1])
            k[6]=int(-3*imagePad[i-1,j-1])+int(-3*imagePad[i,j-1])+int(-3*imagePad[i-1,j])+int(5*imagePad[i-1,j+1])                 +int(5*imagePad[i,j+1])+int(-3*imagePad[i+1,j-1])+int(-3*imagePad[i+1,j])+int(5*imagePad[i+1,j+1])
            k[7]=int(-3*imagePad[i-1,j-1])+int(-3*imagePad[i,j-1])+int(-3*imagePad[i-1,j])+int(-3*imagePad[i-1,j+1])                 +int(5*imagePad[i,j+1])+int(-3*imagePad[i+1,j-1])+int(5*imagePad[i+1,j])+int(5*imagePad[i+1,j+1])
            graident=max(k)
            if graident>threshold:
                output[i-1,j-1]=0
            else:
                output[i-1,j-1]=255
    return output


# In[ ]:


#test
src=cv2.imread("lena.bmp",0)
test=kirschCompassOperator(src,135)
cv2.imwrite("kirsch.bmp",test)


# In[ ]:


def robinsonCompassOperator(image,threshold):
    rows,cols=image.shape
    output=np.zeros(shape=image.shape)
    imagePad=np.pad(image,((1,1),(1,1)),'reflect')
    for i in range(1,513):
        for j in range(1,513):
            r=np.zeros(8)
            """
            1 2 6
            3   7
            4 5 8
            """
            r[0]=int(-1*imagePad[i-1,j-1])+int(0*imagePad[i,j-1])+int(-2*imagePad[i-1,j])+int(-1*imagePad[i-1,j+1])                 +int(0*imagePad[i,j+1])+int(1*imagePad[i+1,j-1])+int(2*imagePad[i+1,j])+int(1*imagePad[i+1,j+1])
            r[1]=int(0*imagePad[i-1,j-1])+int(1*imagePad[i,j-1])+int(-1*imagePad[i-1,j])+int(-2*imagePad[i-1,j+1])                 +int(-1*imagePad[i,j+1])+int(2*imagePad[i+1,j-1])+int(1*imagePad[i+1,j])+int(0*imagePad[i+1,j+1])
            r[2]=int(1*imagePad[i-1,j-1])+int(2*imagePad[i,j-1])+int(0*imagePad[i-1,j])+int(-1*imagePad[i-1,j+1])                 +int(-2*imagePad[i,j+1])+int(1*imagePad[i+1,j-1])+int(0*imagePad[i+1,j])+int(-1*imagePad[i+1,j+1])
            r[3]=int(2*imagePad[i-1,j-1])+int(1*imagePad[i,j-1])+int(1*imagePad[i-1,j])+int(0*imagePad[i-1,j+1])                 +int(-1*imagePad[i,j+1])+int(0*imagePad[i+1,j-1])+int(-1*imagePad[i+1,j])+int(-2*imagePad[i+1,j+1])
            r[4]=int(1*imagePad[i-1,j-1])+int(0*imagePad[i,j-1])+int(2*imagePad[i-1,j])+int(1*imagePad[i-1,j+1])                 +int(0*imagePad[i,j+1])+int(-1*imagePad[i+1,j-1])+int(-2*imagePad[i+1,j])+int(-1*imagePad[i+1,j+1])
            r[5]=int(0*imagePad[i-1,j-1])+int(-1*imagePad[i,j-1])+int(1*imagePad[i-1,j])+int(2*imagePad[i-1,j+1])                 +int(1*imagePad[i,j+1])+int(-2*imagePad[i+1,j-1])+int(-1*imagePad[i+1,j])+int(0*imagePad[i+1,j+1])
            r[6]=int(-1*imagePad[i-1,j-1])+int(-2*imagePad[i,j-1])+int(0*imagePad[i-1,j])+int(1*imagePad[i-1,j+1])                 +int(2*imagePad[i,j+1])+int(-1*imagePad[i+1,j-1])+int(0*imagePad[i+1,j])+int(1*imagePad[i+1,j+1])
            r[7]=int(-2*imagePad[i-1,j-1])+int(-1*imagePad[i,j-1])+int(-1*imagePad[i-1,j])+int(0*imagePad[i-1,j+1])                 +int(1*imagePad[i,j+1])+int(0*imagePad[i+1,j-1])+int(1*imagePad[i+1,j])+int(2*imagePad[i+1,j+1])
            graident=max(r)
            if graident>threshold:
                output[i-1,j-1]=0
            else:
                output[i-1,j-1]=255
    return output


# In[ ]:


#test
src=cv2.imread("lena.bmp",0)
test=robinsonCompassOperator(src,43)
cv2.imwrite("robinson.bmp",test)


# In[41]:


def NevatiaBabuOperator1(image,threshold):
    rows,cols=image.shape
    output=np.zeros(shape=image.shape)
    imagePad=np.pad(image,((2,2),(2,2)),'reflect')
    for i in range(2,514):
        for j in range(2,514):
            N=np.zeros(6)
            N[0]=int(100*imagePad[i-2,j-2])+int(100*imagePad[i-1,j-2])+int(100*imagePad[i,j-2])+int(100*imagePad[i+1,j-2])+int(100*imagePad[i+2,j-2])            +int(100*imagePad[i-2,j-1])+int(100*imagePad[i-1,j-1])+int(100*imagePad[i,j-1])+int(100*imagePad[i+1,j-1])+int(100*imagePad[i+2,j-1])            +int(0*imagePad[i-2,j])+int(0*imagePad[i-1,j])+int(0*imagePad[i,j])+int(0*imagePad[i+1,j])+int(0*imagePad[i+2,j])            +int(-100*imagePad[i-2,j+1])+int(-100*imagePad[i-1,j+1])+int(-100*imagePad[i,j+1])+int(-100*imagePad[i+1,j+1])+int(-100*imagePad[i+2,j+1])            +int(-100*imagePad[i-2,j+2])+int(-100*imagePad[i-1,j+1])+int(-100*imagePad[i,j+1])+int(-100*imagePad[i+1,j+1])+int(-100*imagePad[i+2,j+1])
            
            N[1]=int(100*imagePad[i-2,j-2])+int(100*imagePad[i-1,j-2])+int(100*imagePad[i,j-2])+int(100*imagePad[i+1,j-2])+int(100*imagePad[i+2,j-2])            +int(100*imagePad[i-2,j-1])+int(100*imagePad[i-1,j-1])+int(100*imagePad[i,j-1])+int(78*imagePad[i+1,j-1])+int(-32*imagePad[i+2,j-1])            +int(100*imagePad[i-2,j])+int(92*imagePad[i-1,j])+int(0*imagePad[i,j])+int(-92*imagePad[i+1,j])+int(-100*imagePad[i+2,j])            +int(32*imagePad[i-2,j+1])+int(-78*imagePad[i-1,j+1])+int(-100*imagePad[i,j+1])+int(-100*imagePad[i+1,j+1])+int(-100*imagePad[i+2,j+1])            +int(-100*imagePad[i-2,j+2])+int(-100*imagePad[i-1,j+1])+int(-100*imagePad[i,j+1])+int(-100*imagePad[i+1,j+1])+int(-100*imagePad[i+2,j+1])
            
            N[2]=int(100*imagePad[i-2,j-2])+int(100*imagePad[i-1,j-2])+int(100*imagePad[i,j-2])+int(32*imagePad[i+1,j-2])+int(-100*imagePad[i+2,j-2])            +int(100*imagePad[i-2,j-1])+int(100*imagePad[i-1,j-1])+int(92*imagePad[i,j-1])+int(-78*imagePad[i+1,j-1])+int(-100*imagePad[i+2,j-1])            +int(100*imagePad[i-2,j])+int(100*imagePad[i-1,j])+int(0*imagePad[i,j])+int(-100*imagePad[i+1,j])+int(-100*imagePad[i+2,j])            +int(100*imagePad[i-2,j+1])+int(78*imagePad[i-1,j+1])+int(-92*imagePad[i,j+1])+int(-100*imagePad[i+1,j+1])+int(-100*imagePad[i+2,j+1])            +int(100*imagePad[i-2,j+2])+int(-32*imagePad[i-1,j+1])+int(-100*imagePad[i,j+1])+int(-100*imagePad[i+1,j+1])+int(-100*imagePad[i+2,j+1])
            
            N[3]=int(-100*imagePad[i-2,j-2])+int(-100*imagePad[i-1,j-2])+int(0*imagePad[i,j-2])+int(100*imagePad[i+1,j-2])+int(100*imagePad[i+2,j-2])            +int(-100*imagePad[i-2,j-1])+int(-100*imagePad[i-1,j-1])+int(0*imagePad[i,j-1])+int(100*imagePad[i+1,j-1])+int(100*imagePad[i+2,j-1])            +int(-100*imagePad[i-2,j])+int(-100*imagePad[i-1,j])+int(0*imagePad[i,j])+int(100*imagePad[i+1,j])+int(100*imagePad[i+2,j])            +int(-100*imagePad[i-2,j+1])+int(-100*imagePad[i-1,j+1])+int(0*imagePad[i,j+1])+int(100*imagePad[i+1,j+1])+int(100*imagePad[i+2,j+1])            +int(-100*imagePad[i-2,j+2])+int(-100*imagePad[i-1,j+1])+int(0*imagePad[i,j+1])+int(100*imagePad[i+1,j+1])+int(100*imagePad[i+2,j+1])
            
            N[4]=int(-100*imagePad[i-2,j-2])+int(32*imagePad[i-1,j-2])+int(100*imagePad[i,j-2])+int(100*imagePad[i+1,j-2])+int(100*imagePad[i+2,j-2])            +int(-100*imagePad[i-2,j-1])+int(-78*imagePad[i-1,j-1])+int(92*imagePad[i,j-1])+int(100*imagePad[i+1,j-1])+int(100*imagePad[i+2,j-1])            +int(-100*imagePad[i-2,j])+int(-100*imagePad[i-1,j])+int(0*imagePad[i,j])+int(100*imagePad[i+1,j])+int(100*imagePad[i+2,j])            +int(-100*imagePad[i-2,j+1])+int(-100*imagePad[i-1,j+1])+int(-92*imagePad[i,j+1])+int(78*imagePad[i+1,j+1])+int(100*imagePad[i+2,j+1])            +int(-100*imagePad[i-2,j+2])+int(-100*imagePad[i-1,j+1])+int(-100*imagePad[i,j+1])+int(-32*imagePad[i+1,j+1])+int(100*imagePad[i+2,j+1])
            
            N[5]=int(100*imagePad[i-2,j-2])+int(100*imagePad[i-1,j-2])+int(100*imagePad[i,j-2])+int(100*imagePad[i+1,j-2])+int(100*imagePad[i+2,j-2])            +int(-32*imagePad[i-2,j-1])+int(78*imagePad[i-1,j-1])+int(100*imagePad[i,j-1])+int(100*imagePad[i+1,j-1])+int(100*imagePad[i+2,j-1])            +int(-100*imagePad[i-2,j])+int(-92*imagePad[i-1,j])+int(0*imagePad[i,j])+int(92*imagePad[i+1,j])+int(100*imagePad[i+2,j])            +int(-100*imagePad[i-2,j+1])+int(-100*imagePad[i-1,j+1])+int(-100*imagePad[i,j+1])+int(-78*imagePad[i+1,j+1])+int(32*imagePad[i+2,j+1])            +int(-100*imagePad[i-2,j+2])+int(-100*imagePad[i-1,j+1])+int(-100*imagePad[i,j+1])+int(-100*imagePad[i+1,j+1])+int(-100*imagePad[i+2,j+1])
            
            graident=max(N)
            if graident>threshold:
                output[i-2,j-2]=0
            else:
                output[i-2,j-2]=255
    return output


# In[42]:


#test
src=cv2.imread("lena.bmp",0)
test=NevatiaBabuOperator1(src,12500)
cv2.imwrite("nevatia1.bmp",test)


# In[ ]:




