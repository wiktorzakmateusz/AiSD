

def Hanoi(n, src, tmp, dst):
    if n == 0: return

    Hanoi(n-1, src, dst, tmp)
    dst.append(src.pop())
    Hanoi(n-1, tmp, src, dst)










def main():
    towers = [[8,6,4,2], [], []]

    Hanoi(4, towers[0], towers[1], towers[2])

    print(towers)


if __name__ == '__main__':
    main()