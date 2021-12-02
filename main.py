from random import random
lenth = 10
searched = 20
array = [0] * lenth
for i in range(lenth):
    array[i] = int(random() * 25)
print(array)

def search(arr) :
    for i in range(lenth-1):
        for j in range(i+1, lenth):
            for k in range(i+2, lenth):
                if arr[i] + arr[j] + arr[k] == searched:
                    print("є числа")
                    print(arr[i],arr[j],arr[k])
                    return [arr[i], arr[j], arr[k]]
    print("немає чисел")
search(array)