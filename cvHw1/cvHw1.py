#!/usr/bin/env python
# coding: utf-8

# In[17]:

def main()
	import cv2
	import numpy as np
	from PIL import Image


	# In[18]:


	src= cv2.imread("lena.bmp",cv2.IMREAD_GRAYSCALE)
	width,height=src.shape


	# ## upside-down lena

	# In[19]:


	height


	# In[21]:


	#upDownImg=np.flipud(src)
	for i in range(height):
		for j in range(width):
			upDownImg[i,j]=src[height-i-1,j]
	cv2.imwrite("upSideDown.bmp",upDownImg)


	# ## right-side-left lena

	# In[22]:


	#rightLeftImg=np.fliplr(src)
	for i in range(height):
		for j in range(width):
			rightLeftImg[i,j]=src[i,width-j-1]
	cv2.imwrite("rightSideLeft.bmp",rightLeftImg)


	# ## diagonally mirrored lena 

	# In[5]:


	dialMirrorImg=src.T
	dialMirrorImg.shape
	#cv2.imshow("",dialMirrorImg)
	#waitKey(0)
	#dialMirrorImg= Image.dialMirrorImg
	cv2.imwrite("dialMirrorImg.bmp",dialMirrorImg)

