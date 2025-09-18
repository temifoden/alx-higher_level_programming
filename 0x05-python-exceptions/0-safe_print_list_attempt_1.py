#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0        
    for _ in my_list:
        count += 1
    
    if count < x:
        raise ValueError(f"List have less element than {x}")
    
    try:
        new_list = my_list[:x]
        for num in new_list:
            print(num, end='')
    except IndexError:
        pass

    print()
    return count

    
    