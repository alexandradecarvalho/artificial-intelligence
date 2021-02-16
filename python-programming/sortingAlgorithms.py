#1 - Function that, given a list of numbers, executes selection sort
def numSelectionSort(lista):
    if len(lista) > 1:
        potencial_trader = min(lista[1:])

        if potencial_trader < lista[0]:
            lista[lista.index(potencial_trader)], lista[0] = lista[0], potencial_trader
        
        return [lista[0]] + numSelectionSort(lista[1:]) 
    elif len(lista) == 1:
        return [lista[0]]
    else:
        return []
    
#2 - Function that, given a list of numbers, executes bubble sort
def numBubbleSort(lista): 
    if lista:
        swapped = 0
        for x in range(0, len(lista)-1): 
            if lista[x] > lista[x+1] : 
                lista[x], lista[x+1] = lista[x+1], lista[x]
                swapped = 1

        if swapped:
            return numBubbleSort(lista)
        else:
            return lista
    else:
        return []

#3 - Function that, given a list of numbers, executes quick sort
def numQuickSort(lista):
    if len(lista)>1:
        pivot = lista[-1]
        res = [pivot]
        for element in lista:
            if element > pivot:
                res.append(element)
            elif element != pivot:
                res.insert(0,element)
        
        pivot_idx = res.index(pivot)
        return numQuickSort(res[:pivot_idx]) + [pivot] + numQuickSort(res[pivot_idx+1:])
    elif len(lista) == 1:
        return [lista[0]]
    else:
        return []

#4 - Function that, given a list, executes selection sort
def selectionSort(lista, order):
    if len(lista) > 1:
        potencial_trader = lista[1]
        for x in lista[1:]:
            if order(x,potencial_trader):
                potencial_trader = x

        if order(potencial_trader,lista[0]):
            lista[lista.index(potencial_trader)], lista[0] = lista[0], potencial_trader
        
        return [lista[0]] + selectionSort(lista[1:], order) 
    elif len(lista) == 1:
        return [lista[0]]
    else:
        return []

#5 - Function that, given a list, executes bubble sort
def bubbleSort(lista, order): 
    if lista:
        swapped = 0
        for x in range(0, len(lista)-1): 
            if not order(lista[x],lista[x+1]) : 
                lista[x], lista[x+1] = lista[x+1], lista[x]
                swapped = 1

        if swapped:
            return bubbleSort(lista, order)
        else:
            return lista
    else:
        return []


#6 - Function that, given a list, executes quick sort
def quickSort(lista, order):
    if len(lista)>1:
        pivot = lista[-1]
        res = [pivot]
        for element in lista:
            if order(element,pivot):
                res.insert(0,element)
            elif element != pivot:
                res.append(element)
        
        pivot_idx = res.index(pivot)
        return quickSort(res[:pivot_idx], order) + [pivot] + quickSort(res[pivot_idx+1:], order)
    elif len(lista) == 1:
        return [lista[0]]
    else:
        return []

if __name__ == "__main__":
    print("Testing the numerical algorithms: [64,25,12,22,11] ")
    print("SELECTION SORT: " + str(numSelectionSort([64,25,12,22,11])))
    print("BUBBLE SORT: " + str(numBubbleSort([64,25,12,22,11])))
    print("QUICK SORT: " + str(numQuickSort([64,25,12,22,11])))
    print()
    print("Testing the generic algorithms: ['goncalo',64,25,12,22,'alexa',11] ")
    lesser = lambda x, y: x < y if type(x) == type(y) else True if type(x) == int else False 
    print("SELECTION SORT: " + str(selectionSort(['goncalo',64,25,12,22,'alexa',11], lesser)))
    print("BUBBLE SORT: " + str(bubbleSort(['goncalo',64,25,12,22,'alexa',11], lesser)))
    print("QUICK SORT: " + str(quickSort(['goncalo',64,25,12,22,'alexa',11], lesser)))