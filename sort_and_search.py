

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
    print("Input:", lst, end="\n")
    merge_sort(lst)
    print("Output:", lst, end="\n\n")
            
if __name__ == '__main__':
    
    my_list = [ 9, 5, 1, 5, 5]
    sort_list(my_list)
            
    
    
