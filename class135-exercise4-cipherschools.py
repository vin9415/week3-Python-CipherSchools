def num_to_string(string):
    return [str(i) for i in string if (type(i)==int or type(i)==float)]

print(num_to_string([True,False,[1,2,3],1,1.0,3]))
    