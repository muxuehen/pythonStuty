'''

@author: 
'''
lists = ['4','3','5','1','2']
print lists
lists.sort()
print lists
del lists[0]
print lists
lists.append('1')
print lists
lists.sort()
print lists
print dir()
print dir().__doc__;

print('--------------------')
tuples = ('kfc','m','d')
print tuples
print len(tuples)
print tuples[0]+' ,'+tuples[1]

print('--------------------')
name1 = 'jack'
name2 = 'lucy'
age = 22
print '%s %s %s'% (name1,name2,age)
print name1[1]

print('--------------------')
dics = {
        'girl':'lucy',
        'boy':'jack',
        'girlAddress':'NewYork',
        'boyAddress':'Paris'
        }
print dics['girlAddress']
dics['girlAge'] = 12
print dics
del dics['boy']
print dics

print('--------------------')
sequences = ['jack','lucy','joe','lily','mark','rose'];
print sequences[1:3]
print sequences[1:]

print('--------------------')
strs = 'jacklovelucy'
print strs.startswith('ja')
print strs.find('l')
strList = ['jack','love','lucy']
dots = '_*_'
print dots.join(strList);
