
import random










def create_list(n):

    pula = []
    for i in range(n):
        pula.append(i)

    lista = [0]*n

    head = random.choice(pula)
    pula.remove(head)
    act = random.choice(pula)
    pula.remove(act)
    lista[head] = [random.randint(1,2*n), act]

    for i in range(n-2):
        next = random.choice(pula)
        pula.remove(next)
        lista[act] = [random.randint(1,2*n), next]
        act = next

    lista[next] = [random.randint(1,2*n), -1]


    return lista, head


def printAll(lista, head):
    print("lista: " + str(lista) + f"\nhead : {head}")
    i = head

    while i != -1:
        print(lista[i][0], end = " ")
        i = lista[i][1]

    print("")



def insert(lista, head, v):
    lista.append([v, head])
    head = len(lista) - 1

    return lista, head


def main():
    '''
    lista, head = create_list(4)
    printAll(lista, head)

    lista, head = insert(lista, head, 15)
    printAll(lista, head)
    '''




if __name__ == '__main__':
    main()