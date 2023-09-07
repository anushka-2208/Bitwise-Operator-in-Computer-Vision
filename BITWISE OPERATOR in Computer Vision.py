#!/usr/bin/env python
# coding: utf-8

# # BITWISE OPERATOR in Computer Vision

# In[1]:


#importing OpenCV
import cv2

#reading both binary images
img1 = cv2.imread(r'C:\Users\lenova\Desktop\image1.png')
img2 = cv2.imread(r'C:\Users\lenova\Desktop\image2.png')


# In[5]:


# bitwise operator (OR) result
res_or = cv2.bitwise_or(img1,img2)

#showing results
cv2.imshow("OR Result" , res_or)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[6]:


# bitwise operator (AND) result
res_and = cv2.bitwise_and(img1,img2)

#showing results
cv2.imshow("AND Result" , res_and)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[8]:


# bitwise operator (XOR) result
res_xor = cv2.bitwise_xor(img1,img2)

#showing results
cv2.imshow("XOR Result" , res_xor)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[9]:


# bitwise operator (NOT) result
res_not = cv2.bitwise_not(img1,img2)

#showing results
cv2.imshow("NOT Result" , res_not)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




