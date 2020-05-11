from heapq import *
from random import shuffle

print("1 - heappush")
data = list(range(10))
shuffle(data)
heap = []
for n in data:
    heappush(heap,n)
print(data,heap)
print("Lógica: Elemento na posição  i é menor que os na posição 2*i e 2*i +1")
input()

for i in range(len(heap)):
    print("i:   ",i,"-->",heap[i])
    try:
        print("2i:  ",2*i, "-->",heap[2*i])
        print("2i + 1:  ",2*i+1,"-->",heap[2*i+1])
    except:
        break    