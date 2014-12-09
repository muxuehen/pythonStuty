#coding=utf-8
'''
中文
@author:
'''
class Fibs:
    def fibs(self,num):
        result = [0,1]
        for i in range(num-2):
            result.append(result[-2] + result[-1])
        return result
    
f = Fibs()
print f.fibs(10)
