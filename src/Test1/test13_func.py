#coding=utf-8
'''

@author: 
'''
#mapʹ使用一
print map(str, range(10))
#mapʹ使用二
def addH(x):
    return x+100
h = [1,2,3]
print map(addH, h)

#filter使用一
def func(x):
    return x.isalnum()
seq = ["foo","x41","?!",'15',"**"]
print filter(func, seq)
#filter使用二
print [x for x in ['abc','123','()'] if x.isalnum()]
#filter使用三
print filter(lambda x : x.isalnum(),['abc','123','()'])

#reduce用法(求和)
print reduce(lambda x,y: x+y, [1,2,3,4,5])
