
def maks_pod(tab):
    n = len(tab)  #dlugosc tablicy
    start = 0
    stop = 0
    max_sum = 0                       #4


    for i in range(n):                  #n
        for j in range(i, n):           #n-i
            act_sum = 0                 #1
            for k in range(i, j + 1):   #j-i
                act_sum += tab[k]       #3
            if act_sum > max_sum:       #1
                start = i
                stop = j
                max_sum = act_sum       #4
    return start, stop, max_sum         #3

def main():
    tab = [1,4,-5,3]
    print(maks_pod(tab))  #O(n^3    )

if __name__ == '__main__':
    main()






