# -*- coding: utf-8 -*-
'''
磨皮算法
Dest =(Src * (100 - Opacity) + (Src + 2 * GuassBlur(EPFFilter(Src) - Src + 128) - 256) * Opacity) /100 ;
'''
import cv2
import numpy as np
def beauty_face(img):
	dst = np.zeros_like(img)
	# v1, v2 磨皮程度与细节程度的确定
	v1 = 3
	v2 = 1
	# dx, fc 双边滤波参数之一
	dx = v1 * 5
	fc = v1 * 12.5
	# 透明度
	p = 0.1
	temp4 = np.zeros_like(img)
	# 双边滤波
	temp1 = cv2.bilateralFilter(img,dx,fc,fc)
	temp2 = cv2.subtract(temp1,img);
	temp2 = cv2.add(temp2,(10,10,10,128))
	# 高斯模糊
	temp3 = cv2.GaussianBlur(temp2,(2*v2 - 1,2*v2-1),0)
	temp4 = cv2.add(img,temp3)
	dst = cv2.addWeighted(img,p,temp4,1-p,0.0)
	dst = cv2.add(dst,(10, 10, 10,255))
	return dst
# 输入照片源
img = cv2.imread('./zhaopian.jpg')
dst = beauty_face(img)
cv2.imshow("SRC",img)
cv2.imshow("DST",dst)
cv2.waitKey()
cv2.destroyAllWindows()