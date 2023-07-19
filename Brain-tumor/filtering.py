import numpy as np
import cv2
from scipy import stats


#read image
img_src = cv2.imread('7.jpg')

#prepare the 5x5 shaped filter
kernel = np.array([[1, 1, 1, 1, 1], 
                   [1, 1, 1, 1, 1], 
                   [1, 1, 1, 1, 1], 
                   [1, 1, 1, 1, 1], 
                   [1, 1, 1, 1, 1]])
kernel = kernel/sum(kernel)

#filter the source image
img_rst = cv2.filter2D(img_src,-1,kernel)

#save result image
cv2.imwrite('7Result.jpg',img_rst)


 

MSE = np.square(np.subtract(img_src,img_rst)).mean()

print ("\n MSE : ",  MSE)

axis = 0

ddof = 0

a = np.asanyarray(img_rst)
m = a.mean(axis)
sd = a.std(axis=axis, ddof=ddof)

SNR_IM = np.where(sd == 0, 0, m/sd)

print ("\n SNR  : ",   SNR_IM)



 

