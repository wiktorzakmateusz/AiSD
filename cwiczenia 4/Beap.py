

def ij2k(i,j):
    #if i == 0 or j == 0:
        #return None
    return int(i*(i-1)/2 + j)

def k2ij(k):
    sum = 0
    i = 1
    while sum + i < k:
        sum += i
        i += 1

    j = k - sum

    return i, j

def up_beap(beap, k):
    i,j = k2ij(k)


    while True:
        if i == 1:
            return
        if j-1 == 0:
            smaller_el_id = ij2k(i-1, j)

        elif j > i-1:
            smaller_el_id = ij2k(i-1, j-1)

        else:
            smaller_el_id = ij2k(i-1, j-1)
            if beap[smaller_el_id] > beap[smaller_el_id + 1]:
                smaller_el_id += 1

        if beap[smaller_el_id] < beap[k]:
            beap[smaller_el_id], beap[k] = beap[k], beap[smaller_el_id]
            k = smaller_el_id
            i,j = k2ij(k)
        else:
            return

def down_beap(beap, k):
    n = len(beap) - 1
    i,j = k2ij(k)

    while True:
        if ij2k(i+1,j) <= n:
            bigger_el_id = ij2k(i+1,j)
            if ij2k(i+1,j+1) <= n and beap[bigger_el_id] < beap[bigger_el_id + 1]:
                bigger_el_id += 1
            if beap[k] < beap[bigger_el_id]:
                beap[bigger_el_id], beap[k] = beap[k], beap[bigger_el_id]
                k = bigger_el_id
                i, j = k2ij(k)
            else:
                return

        else:
            return

def del_max(beap):
    beap[1] = beap[len(beap) - 1]
    beap = beap[:-1]
    down_beap(beap, 1)

    return beap

def insert(beap, v):
    beap.append(v)
    up_beap(beap, len(beap) - 1)

def find_last_full_el(beap):
    n = len(beap) - 1
    sum = 0
    i = 1
    while sum + i <= n:
        sum += i
        i += 1


    return sum

def search(beap, v):
    n = len(beap) - 1
    k = find_last_full_el(beap)
    i, j = k2ij(k)

    while j != 0:
        if v == beap[k]:
            return k

        if v > beap[k]:
            i, j = i-1, j-1
            k = ij2k(i,j)
            continue

        # only v < beap[k] left, so not else needed
        if ij2k(i+1, j) <= n:
            i = i+1
            k = ij2k(i,j)
            continue
        else:
            j -= 1
            k -= 1

    return -1






def main():
    #testing ij2k, k2ij
    #print(ij2k(4,1))
    #print(k2ij(11))


    #demonstration up_beap
    #beap = [0, 10, 7, 8, 4, 20]
    #up_beap(beap, 5)
    #print(beap)


    #demontstration down_beap
    #beap = [0, 5, 10, 20, 7, 8, 5, 4, 3]
    #down_beap(beap, 1)
    #print(beap)


    #demonstration del_max
    #beap = [0, 20, 10, 8, 7, 5, 5, 4, 3]
    #beap = del_max(beap)
    #print(beap)


    #demonstration insert
    #beap = [0, 10, 7, 8, 4, 5, 6, 3]
    #insert(beap, 9)
    #print(beap)
    #insert(beap, 7)
    #print(beap)

    #demonstration search
    beap = [0, 30, 15, 20, 8, 7, 3, 6]
    print(search(beap, 15))
    print(search(beap, 9))




if __name__ == '__main__':
    main()