
# %%
print('Hello world')

s = 'Python3 Study'
n = 1
f = 1.54


# %%
print(s)

# %%

count = 0 
while count < 5:
    print(count, 'less than 5')
    count += 1 
else:
    print(count, 'greater or equal 5')

#%%
# number  from 1 to 100  print even 

count = 0
while  count <= 100:
    if count % 2 ==0:
        print (count)
    count += 1 
    
#%%
#define a list and adding value to it 

a = 'tiger'
b = 'giraffe'
animals = ['elephant', 'lion', a, b]
animals 


#%% adding values to list 
animals += ['monkey', 'dog']
animals.append('cat')
animals.extend(['bird'])
animals



#%% update list 
list = ['google', 'microsoft', '1997','2000', '45']
list[3] # array start from 0 print 4th element 


#%%
list[:2] # print fron begginig to 1 last value is not included

#%%
list[::3] #prints first and 4 values 


#%%
list[1] = 'Uber' #replace the value 1 for new item 
list 


#%%
#delete from list 
list2  = ['google', 'microsoft', '1997','2000', '45']
list.remove('google')
del list[2]
list2

#%%

print(list2.pop())
print(list2)

#%%
#try it out 
#write a list with 2 types of fruits 
fruits = ['kiwi', 'grapefruit']
fruits


#%%add 3 to it 
fruits += ['orange','apple','banana']
fruits


#%%swap the second with the 3rd one 
swap = fruits[1]
fruits[1] = fruits[2]
fruits[2] = swap
fruits


#%%remove last one 
#fruits.pop()
#fruits 

del fruits[4]
fruits

#%%remove second fron the list 
del fruits[1]
fruits

#%%
