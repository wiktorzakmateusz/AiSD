
def down_heap(heap, i):
    n = len(heap) - 1

    while n >= 2*i:
        k = 2*i
        if (2*i+1) <= n and heap[k+1] > heap[k]:
            k += 1

        if heap[k] <= heap[i]:
            break

        heap[k], heap[i] = heap[i], heap[k]

        i = k


def up_heap(heap, i):

    while i // 2 >= 1 and heap[i] > heap[i//2]:
        heap[i], heap[i//2] = heap[i//2], heap[i]
        i = i // 2

def insert_heap(heap, v):
    heap.append(v)
    n = len(heap) - 1
    up_heap(heap, n)

def building_heap_worse_solution(list_of_elements):
    heap = [0]
    for v in list_of_elements:
        insert_heap(heap, v)

    return heap

def building_heap_better_solution(list_of_elements):
    heap = list_of_elements
    heap.insert(0, 0) #zmienia tez list_of_elements

    n = len(heap) - 1
    for i in reversed(range(n//2)):
        down_heap(heap, i+1)
    return heap

def find_last_full_row(n):
    i = 0
    sum = 1
    while sum <= n:
        i += 1
        sum  = sum + (2**i)

    return i-1


def main():

    #demonstration down_heap()

    #heap = [0, 3, 10, 8, 7, 9]
    #down_heap(heap, 1)
    #print(heap)


    #demonstration up_heap()

    #heap = [0, 20, 10, 8, 7, 21]
    #up_heap(heap, 5)
    #print(heap)


    #demonstration insert_heap()

    #heap = [0, 20, 10, 8, 7, 9]
    #insert_heap(heap, 21)
    #print(heap)


    #demonstration building_heap_worse_solution()

    #heap = building_heap_worse_solution([10, 7, 8, 20, 9, 5, 22])
    #print(heap)


    #demonstration buidling_heap_better_solution()

    #heap = building_heap_better_solution([10, 7, 8, 20, 9, 5, 22, 30, 40])
    heap = building_heap_better_solution([1, 10, 40, 80, 100, 140])
    print(heap)


if __name__ == '__main__':
    main()