# Punto 2 : metodo que ordena una lista de manera recursiva con el algoritmo merge sort
# el cual se basa en la estrategia de dividir y juntar
def merge_sort(lst):
    
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        rear = lst[mid:]
        
        merge_sort(left)
        merge_sort(rear)
        i = j = k = 0

        while i < len(left) and j < len(rear):
            if left[i] < rear[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = rear[j]
                j += 1
            k += 1
            
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1
            
        while j < len(rear):
            lst[k] = rear[j]
            j += 1
            k += 1

def sort_list(lst):
    lst_aux = lst.copy()
    merge_sort(lst_aux)
    print("Input: ", lst)
    print("Output: ", lst_aux, end="\n\n")
    return lst_aux
    
    
    
# Punto 3: metodo que crea el arbol binario de busqueda
# Recibe una lista de numeros enteros
# Devuelve un arbol binario de busqueda donde un nodo se representa de la siguiente manera:
# [key, left_subtree, right_subtree]
def create_bts(lst):
    tree = []
    if len(lst) == 0:
        return None
    else:
        if len(lst) == 1:
            return lst
        else:
            mid = len(lst) // 2
            left = lst[:mid]
            right = lst[mid+1:]
            
            tree.append(lst[mid])
            tree.append(create_bts(left))
            tree.append(create_bts(right))
        
    return tree


# Punto 4: metodo que realiza la busqueda en el arbol binario de busqueda
# basado en el la representacion del punto 3 para un arbol binario de busqueda
# el cual recibe una lista de numeros enteros y un numero entero a buscar
# y retorna True si el numero esta en el arbol binario de busqueda y la profundidad de la busqueda
def search_bts(tree, key, depth=0):
    
    
    if tree == None:
        print("Tree is empty: ", key)
        return False
    else:
        if tree[0] == key:
            print("Key found: ", key, " at depth: ", depth)
            return True
        else:
            if len(tree) == 1:
                print("Key not found: ", key)
                return False
            else:
                if key < tree[0]:
                    return search_bts(tree[1], key, depth+1)
                else:
                    return search_bts(tree[2], key, depth+1)

      
if __name__ == '__main__':
    
    # Lista de numeros enteros no ordenada
    my_list = [ 4, 7, 1, 5, 3, 6, 2]
    
    # Lista de numeros enteros ordenada
    output = sort_list(my_list)
    
    # Inicializacion del arbol binario de busqueda
    bts_list = create_bts(output)
    print("Binary tree = ",bts_list, end="\n\n")   
    
    # Busqueda de un numero en el arbol binario de busqueda
    search_bts(bts_list, 3)
    
    
