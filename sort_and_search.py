
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
    print("Output: ", lst_aux)
    return lst_aux
    
    
    
# Punto 3
def convert_list_to_bts(lst):
    intput_list = lst.copy()
    bts_lst = []
    
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    
    bts_lst.append(convert_list_to_bts(left))
    
    
    return bts_list



def create_bts(lst):
    cosa = []
    if len(lst) == 0:
        return None
    else:
        if len(lst) == 1:
            cosa.append(lst[0])
            return lst[0]
        else:
            mid = len(lst) // 2
            left = lst[:mid]
            right = lst[mid+1:]
            
            
            print(left)
            print(right)
            
            create_bts(left)
            create_bts(right)
        
    return cosa
    

    
          
if __name__ == '__main__':
    
    my_list = [ 4, 7, 1, 5, 3, 6, 2]
    output = sort_list(my_list)
            
    #print(convert_list_to_bts(output))
    
    print(create_bts(output))
    #mid_node_index = len(my_list) // 2
    #binnary_tree = bts(my_list, 3)
    #print("Binary Tree:", binnary_tree)
    
    
