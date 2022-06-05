
# Punto 2
from numpy import rint


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
    
    
    
# Punto 3
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


# Punto 4 
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
    
    my_list = [ 4, 7, 1, 5, 3, 6, 2, 8]
    #my_list = [ 1,2,3,4,5,6,7]
    output = sort_list(my_list)
    
    bts_list = create_bts(output)
    print("Binary tree = ",bts_list, end="\n\n")    
    
    search_bts(bts_list, 3)
    
    
