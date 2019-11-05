
# coding: utf-8

# In[25]:

import numpy as np
import cv2
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
import os


# In[26]:

get_ipython().system('..\\\\Maintenance\\\\tx3cacti_rangeday_.exe -g 9177')


# In[27]:

IMG_SIZE = 224
img_path = ".//tx3cacti_png//9177//tx3cacti_9177_2019-11-03_2019-11-04.png"
img = cv2.imread(img_path, cv2.IMREAD_COLOR)
img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
print(img.shape)


# In[28]:

import cv2
import numpy as np

lower_blue=np.array([110,50,50])
upper_blue=np.array([130,255,255])

lower_green = np.array([0,180,0]) 
upper_green = np.array([100,255,255])

img_wgq = cv2.imread(".//tx3cacti_png//9177//tx3cacti_9177_2019-11-03_2019-11-04.png")
xsize,ysize,channel = img_wgq.shape
#调整图片大小
img_wgq = cv2.resize(img_wgq, (ysize//2,xsize//2))

frame = cv2.cvtColor(img_wgq, cv2.COLOR_BGR2HSV)
mask_blue = cv2.inRange(frame, lower_blue, upper_blue)
res_blue = cv2.bitwise_and(frame, frame, mask=mask_blue)
res_blue = cv2.cvtColor(res_blue, cv2.COLOR_HSV2BGR)
#cv2.imshow("mask_blue",mask_blue)
#cv2.imshow("res_blue",res_blue)

frame_green = cv2.cvtColor(img_wgq, cv2.COLOR_BGR2HSV)
mask_green = cv2.inRange(frame_green, lower_green, upper_green)
res_green = cv2.bitwise_and(frame_green, frame_green, mask=mask_green)
res_green = cv2.cvtColor(res_green, cv2.COLOR_HSV2BGR)

#cv2.waitKey(0)
#cv2.destroyAllWindows()


# In[29]:

plt.imshow(res_green)
plt.show()


# In[30]:

g_wgq = cv2.cvtColor(res_green, cv2.COLOR_BGR2GRAY)

ret, g_wgq = cv2.threshold(g_wgq, 100, 100, 0)

#binary , contours, hierarchy = cv2.findContours(g_wgq, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
binary , contours, hierarchy = cv2.findContours(g_wgq, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

ret = cv2.drawContours(img_wgq, contours, -1, (0, 0,255), 2)

plt.imshow(ret)
plt.show()


# In[31]:

total_areas = 0
areas = []
for c in contours[1:]:
    areas.append(cv2.contourArea(c))
    
print(areas)

for ta in areas:
    total_areas += ta

print("所圈面积是: ", total_areas)


# In[ ]:




# In[32]:

IMG_SIZE = 224
img_path = ".//tx3cacti_png//9177//tx3cacti_chj_9177_2019-11-03_2019-11-04.png"
img = cv2.imread(img_path, cv2.IMREAD_COLOR)
img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
print(img.shape)


# In[33]:

import cv2
import numpy as np

lower_blue=np.array([110,50,50])
upper_blue=np.array([130,255,255])

lower_green = np.array([0,180,0]) 
upper_green = np.array([100,255,255])

img_chj = cv2.imread(".//tx3cacti_png//9177//tx3cacti_chj_9177_2019-11-03_2019-11-04.png")
xsize,ysize,channel = img_chj.shape
#调整图片大小
img_chj = cv2.resize(img_chj, (ysize//2,xsize//2))

frame = cv2.cvtColor(img_chj, cv2.COLOR_BGR2HSV)
mask_blue = cv2.inRange(frame, lower_blue, upper_blue)
res_blue = cv2.bitwise_and(frame, frame, mask=mask_blue)
res_blue = cv2.cvtColor(res_blue, cv2.COLOR_HSV2BGR)
#cv2.imshow("mask_blue",mask_blue)
#cv2.imshow("res_blue",res_blue)

frame_green = cv2.cvtColor(img_chj, cv2.COLOR_BGR2HSV)
mask_green = cv2.inRange(frame_green, lower_green, upper_green)
res_green = cv2.bitwise_and(frame_green, frame_green, mask=mask_green)
res_green = cv2.cvtColor(res_green, cv2.COLOR_HSV2BGR)


# In[34]:

plt.imshow(res_green)
plt.show()


# In[35]:

g_chj = cv2.cvtColor(res_green, cv2.COLOR_BGR2GRAY)

ret, g_chj = cv2.threshold(g_chj, 100, 100, 0)

#binary , contours, hierarchy = cv2.findContours(g_wgq, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
binary , contours, hierarchy = cv2.findContours(g_chj, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

ret = cv2.drawContours(img_chj, contours, -1, (0, 0,255), 2)

plt.imshow(ret)
plt.show()


# In[36]:

total_areas = 0
areas = []
for c in contours[1:]:
    areas.append(cv2.contourArea(c))
    
print(areas)

for ta in areas:
    total_areas += ta

print("所圈面积是: ", total_areas)

