
def maks_pod(tab):
    n = len(tab)  #dlugosc tablicy
    start = 0
    stop = 0
    max_sum = tab[0]
    act_sum = 0
    i = 0

    for j in range(n):
        act_sum += tab[j]
        if act_sum > max_sum:
            max_sum = act_sum
            start = i
            stop = j
        if act_sum < 0:
            i = j + 1
            act_sum = 0

    return start, stop, max_sum

def main():
    tab = [-3, -2, -2]
    print(maks_pod(tab))  #O(n^2)

if __name__ == '__main__':
    main()






