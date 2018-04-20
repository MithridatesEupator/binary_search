final_bool = False
def binary_search(array, value):
    global final_bool
    midpoint_value = array[len(array)//2 - 1]
    if midpoint_value == value:
        final_bool = True
    elif len(array) == 1:
        if final_bool != True:
            final_bool = False
        else:
            final_bool = True
    elif value < midpoint_value:
        mid = len(array) // 2
        new_array = array[0:mid]
        binary_search(new_array,value)
    elif value > midpoint_value:
        mid = len(array) // 2
        new_array = array[mid:len(array)]
        binary_search(new_array, value)
    return final_bool