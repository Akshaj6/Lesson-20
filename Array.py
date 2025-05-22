import array as arr
a = arr.array('i', [1, 2, 3, 4])
print("The original array :" +str(a))
print("Number of occurences of number '3' in the array :" +str(a.count(3)))
a.reverse()
print("Reversing the order of itmes :")
print(str(a))