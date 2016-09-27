#coding:utf-8
import math
def getLength(reData):
	reDatas = reData.split()
	return len(reDatas)
def stringToNums(reData):
	reDatas = reData.split()
	length = getLength(reData)
	nums = [0]*length
	for i in range(length):
		nums[i] = float(reDatas[i])
	return nums
def calVari(nums):
	averOfNums = sum(nums)/len(nums)
	sumOfValues = 0
	for i in range(len(nums)):
		singOfValues = (nums[i]-averOfNums)**2
		sumOfValues += singOfValues
	return sumOfValues/len(nums) 
def getBessel(expResults):
	numsResults = stringToNums(expResults)
	variOfResults = calVari(numsResults)
	return math.sqrt(variOfResults)
def getMultiple(nums):
	multiples = {3:4.3 , 4:3.18 , 5:2.78 , 6:2.57 , 7:2.45 , 8:2.36 , 9:2.31 , 10:2.26 , 15:2.14 , 20:2.09}
	return multiples.get(nums)/math.sqrt(nums)
datas = raw_input('输入实验结果\n')
aClass = getBessel(datas)*getMultiple(getLength(datas))
print('A类不确定度为%f'%aClass)
def getBClass(precsn):
	precsn = input('输入最小刻度值\n')
	return precsn/2
def getUncertn(a,b):
	return math.sqrt((a**2)+(b**2))
#print('不确定度为%f'%getUncertn(aClass,getBClass)
a = getUncertn(aClass,getBClass(6))
print(a)
