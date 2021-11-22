from random import random
N = 10
P = 20
arr = [0] * N
for i in range(N):
    arr[i] = int(random() * 25)
print(arr)

for i in range(N-1):
    for j in range(i+1, N):
        if arr[i] + arr[i+1] + arr[j] == P:
            print("є")
            print(arr[i],arr[i+1],arr[j])
            quit()
print("немає чисел")
