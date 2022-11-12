
def maks_pod(tab):
    n = len(tab)  #dlugosc tablicy
    start = 0
    stop = 0
    max_sum = 0


    for i in range(n):
        act_sum = 0
        for j in range(i, n):
            act_sum += tab[j]
            if act_sum > max_sum:
                start = i
                stop = j
                max_sum = act_sum
    return start, stop, max_sum

def main():
    tab = [1,4,-5,3, 10, -5]
    print(maks_pod(tab))  #O(n^2)

if __name__ == '__main__':
    main()






