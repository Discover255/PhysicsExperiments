#coding:utf-8
import math
def stringToNums(reData):
	reDatas = reData.split()
	length = len(reDatas)
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
def getBessel(numsResults):
	variOfResults = calVari(numsResults)
	return math.sqrt(variOfResults)
def getMultiple(nums):
	if nums<3:
		print("输入的数据小于三组，无法计算")
		return 0.0
	else:
		multiples = {3:4.3 , 4:3.18 , 5:2.78 , 6:2.57 , 7:2.45 , 8:2.36 , 9:2.31 , 10:2.26 , 15:2.14 , 20:2.09}
		return multiples.get(nums)/math.sqrt(nums)
#aClass = getBessel(stringToNums(datas))*getMultiple(len(stringToNums(datas)))
#这是A类不确定度计算总式print('A类不确定度为%f'%aClass)
#precsn = input('输入最小刻度值\n')
def getBClass(precsn):
	return precsn/2
def getUncertn(a,b):
	return math.sqrt((a**2)+(b**2))
#print('不确定度为%f'%getUncertn(aClass,getBClass)
#a = getUncertn(aClass,getBClass(float(precsn)))
#print(a)
