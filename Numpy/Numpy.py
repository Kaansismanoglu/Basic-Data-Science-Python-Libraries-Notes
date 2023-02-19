import numpy as np
np_array = np.array([[1,2,4],[1,3,4],[4,1,4],[4,2,7]])
print(np_array)

#For Matrix .reshape()
np_multi = np_array.reshape(3,4)
print(np_multi)

#For Type
print(type(np_array))

#create 1to10 in list
result = np.arange(0,10)
print("Result: ",result)

#create 1to10 in list with in 3 increments
result2 = np.arange(0,10,3)
print("Result2: ",result2)

#10 times zero, one, two, ...
result3= np.zeros(10)
result4= np.ones(10)
result4 = result4*2
print("Result3: ",result3)
print("Result4: ",result4)

#divide into 5 parts
result5= np.linspace(0,100,5)
print("Result5: ",result5)

#Random
result6 = np.random.randint(0,100)
print("Result6: ",result6)

#Random between 1 and 0
result7 = np.random.rand(2)#Positive
np.random.randn(2)#Negative
print("Result7: ",result7)

#Sum of Rows and Columns in Matrix
print("Result8: ")
print(np_multi.sum(axis=1)) #For Row
print(np_multi.sum(axis=0)) #For Column

#Means and Standard Deviation of List
result9 = np_multi.mean()
result10 = np_multi.std()
print("Result9: ", result9)
print("Result10: ", result10)

#Max and Min Number's Index of List
result11 = np_multi.argmax()
result12 = np_multi.argmin()
print("Result11: ", result11)
print("Result12: ", result12)
print("------------------")

#LIST METHOD WITH INDEX
mylist = np.array([12,23,34,74,65,69,78,80,100,102])
mylist2= np.array([[12,23],[34,74],[65,69],[78,80],[100,102]])
sonuc = mylist[:2]#Limitazation from left
sonuc2 = mylist[3:]#Limitazation from right
sonuc3 = mylist[::]#All of variable
print("Liste: ", mylist)
print("sonuc: ", sonuc)
print("sonuc2: ", sonuc2)
print("sonuc3: ", sonuc3)
print("Eleman 0: ", mylist2[0])
print("Eleman 3: ", mylist2[3])

#List Method 2
sonuc4 = mylist2[1,1]
sonuc5 = mylist2[:,0]
sonuc6 = mylist2[:,0:2]
print("sonuc4: ",sonuc4)
print("sonuc5: ",sonuc5)
print("sonuc6: ",sonuc6)

# NOT: Since the addresses are the same arr2 = arr1 in this situation arr2[0] = 20 like that arr1 is also affected.(Data
# addresses are the same!) To prevent this
arr1 = np.array([1,2,3,4])
arr2 = arr1.copy()
arr2[0] = 7
print("arr1: ", arr1)
print("arr2: ", arr2)
print("---------------------------")

#If you have two list and you want to summation these lists with each other.
list1 = np.random.randint(1,100,6)
list2 = np.random.randint(1,100,6)
print("list1: ",list1)
print("list2: ",list2)
sumof = list1 + list2
print("Sum of these: ", sumof)

#Sin, Cos,Sqrt and Log
sinus = np.sin(list1)
cosine = np.cos(list1)
print("Sin for list 1: ", sinus)
print("Cos for list 1: ", cosine)
Sqrt = np.sqrt(list1)
print("Sqrt for list 1: ", Sqrt)
Logarithm = np.log(list1)
print("Log for list 1: ", Logarithm)

#Vertical and Horizontal
mnumber1 = list1.reshape(2,3)
mnumber2 = list2.reshape(2,3)
print(mnumber1)
print(mnumber2)
matrix = np.vstack((mnumber1,mnumber2)) #Vertical
matrix2 = np.hstack((mnumber1,mnumber2)) #Horizontal
print("Vertical:")
print(matrix)
print("-----------")
print("Horizontal:")
print(matrix2)
print("---------------------")
resbool = list1 >= 50
resbool2 = list1 % 2 == 0
print(list1)
print(resbool)
print(resbool2)#to write which numbers can divide by two with true or false
print(list1[resbool2])#to write which numbers can divide by two with numbers