# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def dicadic_convolution(x,y):
	# Программа для вычисления диадных сверток произвольных векторов или функций (она также называется логической сверткой - "logical convolution"), которую нельзя путать с обычной арифметической сверткой двух функций.
	#   http://caxapa.ru/thumbs/455725/algorithms.pdf  на странице 78 в начале параграфа 5.2 "Dyadic Convolution". Там же дана формула, определяющая диадную свертку. 
	dim=len(x)
	y_={} # приведение к виду y= {0:2,1:4,2:3,3:0,4:2,5:4,6:3,7:0}
	for i in range(dim): y_[i]=y[i]
	y=y_

	def step(d,n): # алгорим синтеза диадосдвиговых матриц индексов пуьем склейки квадрантов
		poprav=np.zeros_like(d)+n	#print poprav  		#d_next = np.append([d,d+poprav],[d+poprav,d], axis=0) 	#poprav = np.array([np.zeros(n)+n]*n)
		d_1 = np.concatenate((d, d+poprav), axis=0) # 1 2 квадранты
		d_2 = np.concatenate((d+poprav, d), axis=0) # 3 4 квадранты
		d_next = np.concatenate((d_1, d_2), axis=1) # итоговая матрица
		return d_next

	# процедура синтеза матриц друг из друга
	ns = 	[2**n for n in range(100)][1:] #[2,4,8,16,32,64] 	#2**n
	#print ns
	ns =ns[:ns.index(dim)]

	for n in ns:
		if n==2: 	
			d = np.array([[0,1],   # исходная диадосдвиговая матрица матрица индексов
				          [1,0]])
			#print n, np.array_str(d)
		 	d = step(d,2)
		 	#print 4, np.array_str(d)
		else:
			d = step(d,n)
			n=n*2
			#print n, np.array_str(d)
		t=[]
		for row in d:
			r=[]
			for i in row:
				r.append(y[i])
			t.append(r)
		t=np.array(t)
		#print t #print '===='

	x=np.array(x)
	return list((x.dot(t))/n)

if __name__ == '__main__':

	x=[3,2,0,1,3,2,0,1]
	y=[2,4,3,0,2,4,3,0]

	print dicadic_convolution(x,y)

	print [3.5,4.75,3.25,2,3.5,4.75,3.25,2]

