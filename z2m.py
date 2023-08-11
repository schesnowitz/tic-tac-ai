string = "hi my name is steve"
def reverse(some_string):
    return some_string[::-1]

# print(reverse(string))   
a =[1,3,5,78]
b = [2,5,9,15]
def merge_sorted_array(arr1, arr2):
    new_array = []
    new_array = arr1 + arr2
    return sorted(new_array)

print(merge_sorted_array(a, b))