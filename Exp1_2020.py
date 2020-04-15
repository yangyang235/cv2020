"""
Task [I] - Demonstrating how to compute the histogram of an image using 4 methods.
(1). numpy based
(2). matplotlib based
(3). opencv based
(4). do it myself (DIY)
check the precision, the time-consuming of these four methods and print the result.
"""


import numpy as np
import matplotlib.pyplot as plt
import cv2
import time
import matplotlib
import scipy
from scipy import ndimage
##
##please coding here for solving Task [I].

# Computing color histogram


#(1). numpy based
# start1 =time.clock()                             #记录开始时间
# def histogram(img, bins):
#     N_x = np.zeros_like(bins, dtype=np.float)   #生成一个与bins相同的全0数组
#     for (i, level) in enumerate(bins):          #一个可遍历的数据对象组合为一个索引序列，同时列出数据和数据下标
#         N_x[i] = np.sum(img == level)
#     return N_x
#
# file = r'C:\yangjiarui\python\fivestart.png'
# imge= cv2.imread(file)
# cv2.imshow('fivestart.png',imge)             #可以在窗口中显示图像。该窗口和图像的原始大小自适应（自动调整到原始尺寸）
# #cv2.waitKey(0)                              #参数表示延迟多少毫秒。默认情况为0。当delay≤0，可以理解为延迟无穷大毫秒，就是暂停了
# #cv2.destroyAllWindows()                     #随便按一个键就会关闭窗口
# plt.figure()
# intensity_levels = np.arange(0,256,1)       #起点为0终点为256步长1
# red_hist= histogram(imge[2,:,:], intensity_levels)#numpy三通道是BGR 所以红色为第三个通道
# end1=time.clock()                            #记录结束时间
# print('Running time: %s Seconds'%(end1-start1))#运行时间
# plt.plot(intensity_levels, red_hist,   color='red')#intensity_levels x轴数据 red_hist y轴 color='red'将颜色设为红色
# plt.show()



#(2). matplotlib based
# start2 =time.clock()
# file = r'C:\yangjiarui\python\fivestart.png'
# imge= cv2.imread(file)
# cv2.imshow('fivestart.png',imge)
# plt.hist(imge[:,:,0].ravel(),256,[0,255]) #hist(数据源, 像素级) 数据源：必须是一维数组,可通过ravel()将三维数组转为一维数组256表示[0,255]
# end2=time.clock()                           #matplotlib为RGB
# print('Running time: %s Seconds'%(end2-start2))
# plt.show()                         #

#(3). opencv based
# start3 =time.clock()
# file = r'C:\yangjiarui\python\fivestart.png'
# imge= cv2.imread(file)
# cv2.imshow('fivestart.png',imge)
# img=cv2.calcHist(imge, [2], None, [256], [0, 256])      #BRG
# end3=time.clock()
# print('Running time: %s Seconds'%(end3-start3))
# plt.figure()                                            #calcHist(图片,需要计算直方图的通道,无视，将颜色取值等分为256份，颜色值取值范围)
# plt.plot(img)
# plt.show()

"""
Task [II]Refer to the link below to do the gaussian filtering on the input image.
Observe the effect of different @sigma on filtering the same image.
Try to figure out the gaussian kernel which the ndimage has used [Solution to this trial wins bonus].
https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.gaussian_filter.html
"""

###
#please coding here for solving Task[II]

# file = r'C:\yangjiarui\python\fivestart.png'
# imge= cv2.imread(file)
# cv2.imshow('fivestart.png',imge)
#
# imge1=ndimage.gaussian_filter(imge,sigma=10)
# plt.imshow(imge1)
# plt.show()




"""
Task [III] Check the following link to accomplish the generating of random images.
Measure the histogram of the generated image and compare it to the according gaussian curve
in the same figure.
"""

###
#please coding here for solving Task[III]

# imge = np.random.multivariate_normal((3,3,3), np.eye(3), (256*256))#不知道，照着函数输入参数要求随便打的
# plt.hist(imge.ravel(),128)#有参数bins,会将数据集按照bins的个数统计;没有bins参数时，默认将数据集分成10个bin展示
# plt.show()

