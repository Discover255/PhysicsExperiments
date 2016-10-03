# -*- coding:utf-8 -*-
import math 
import uncertnty
L = float(input("输入L(以下以毫米为单位)\n"))
D = float(input("输入D\n"))
H = float(input("输入H\n"))
di = input("输入直径\n")
d0 = float(input("输入零差\n"))
ad = sum(uncertnty.stringToNums(di))/len(uncertnty.stringToNums(di))
d = ad - d0
x = [0]*10
print("输入x+和x-")
xp = uncertnty.stringToNums(input("输入x+："))
xm = uncertnty.stringToNums(input("输入x-："))
x = list(map(lambda x,y:(x+y)/2,xp,xm))
dx = list(map(lambda x,y:x-y,x[5:9],x[0:4]))
adx = sum(dx)/float(len(dx))
def getE(m,L,H,d,D,dx):
	g = 9.8
	return (8*m*g*L*H*(10**6))/(math.pi*d*d*D*dx)
E1 = getE(5,L,H,ad,D,adx)
print("L:%s\nH:%s\nd:%s\nD:%s\ndx:%s\n"%(L,H,ad,D,adx))
print(E1)
format(E1,'.15e')
#此程序略去了不确定度的计算
