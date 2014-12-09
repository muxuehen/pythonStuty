'''

@author: zxl
'''
class Person:
    pass #aa
p = Person() 
print p

class Food:
    def sayHi(self):
        print 'hi'
    def sayHello(self,obj):
        print 'hello '+obj
f = Food()
f.sayHi()
f.sayHello('jack')

class Animal:
    def __init__(self, name):
        self.name = name
    def dog(self,obj):
        print 'dog '+ self.name +' '+obj
        
ani = Animal('pp')
ani.dog('ww')
