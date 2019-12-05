#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2


# In[2]:


src=cv2.imread("lena.bmp",cv2.IMREAD_GRAYSCALE)
#hw2實做過的function
rows,cols=src.shape
srcBinary=np.zeros(shape=src.shape,dtype=src.dtype)
for i in range (rows):
    for j in range(cols):
        if src[i,j]>128:
            srcBinary[i,j]=255
        else:
            srcBinary[i,j]=0
cv2.imwrite("lenaBinary.png",srcBinary)


# In[3]:


def downsampling (image,sampleFactor):
    rows,cols=image.shape
    rowsD=int(rows/sampleFactor)
    colsD=int(cols/sampleFactor)
    downsampleImg=np.zeros(shape=(rowsD,colsD),dtype=image.dtype)
    for i in range(rowsD):
        for j in range(colsD):
            downsampleImg[i,j]=image[i*sampleFactor,j*sampleFactor]
    return downsampleImg


# In[4]:


downsample=downsampling(srcBinary,8)
cv2.imwrite("downsampleImg.png",downsample)


# In[72]:


def fYokoi(a1,a2,a3,a4):
    if ([a1,a2,a3,a4].count('r')==4):
        return str(5)
    else:
        return str([a1,a2,a3,a4].count('q'))


# In[64]:


def hYokoi(b,c,d,e):
    if b==c and (d!=b or e!=b):
        return'q'
    elif b==c and (d==b and e==b):
        return'r'
    elif b!=c:
        return's'


# In[93]:


def getNeighborPixels (image,position):
    positionX,positionY=position
    neighborhoodPixels=np.zeros(9)
    for i in range(3):
        for j in range(3):
            dstX=positionX+(i-1)
            dstY=positionY+(j-1)
            if((0<=dstX<image[0].size) and (0<=dstY<image[1].size)):
                neighborhoodPixels[3*j+i]=image[dstX,dstY]
            else:
                neighborhoodPixels[3*j+i]=0
    neighborhoodPixels=[neighborhoodPixels[4],neighborhoodPixels[5],neighborhoodPixels[1]
                       ,neighborhoodPixels[3],neighborhoodPixels[7],neighborhoodPixels[8]
                       ,neighborhoodPixels[2],neighborhoodPixels[0],neighborhoodPixels[6]]
    return neighborhoodPixels


# In[94]:


def yokoiConnectivityNumber(image):
    rows,cols=image.shape
    connectNum = np.chararray(shape=image.shape,unicode=True)
    for i in range(rows):
        for j in range(cols):
            if(image[i,j]!=0):
                neighborhoodPixels= getNeighborPixels(image,(i,j))
                a1= hYokoi(neighborhoodPixels[0],neighborhoodPixels[1],neighborhoodPixels[6],neighborhoodPixels[2])
                a2= hYokoi(neighborhoodPixels[0],neighborhoodPixels[2],neighborhoodPixels[7],neighborhoodPixels[3])
                a3= hYokoi(neighborhoodPixels[0],neighborhoodPixels[3],neighborhoodPixels[8],neighborhoodPixels[4])
                a4= hYokoi(neighborhoodPixels[0],neighborhoodPixels[4],neighborhoodPixels[5],neighborhoodPixels[1])
                connectNum[i,j]=fYokoi(a1,a2,a3,a4)
            else:
                connectNum[i,j]=' '
            if connectNum[i,j]=='0':
                connectNum[i,j]=' '
    return connectNum


# In[95]:


Yokoi=yokoiConnectivityNumber(downsample)
print(Yokoi)


# In[96]:


np.savetxt('Yokoi.txt',Yokoi,delimiter=' ',fmt="%s")


# In[ ]:




