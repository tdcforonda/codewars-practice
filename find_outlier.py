def find_outlier(integers):
    even = []
    even_numbers = 0
    odd = []
    odd_numbers = 0
    
    for number in integers:
        if number %2 == 0:
            even.append(number)
            even_numbers += 1
        elif number %2 == 1:
            odd.append(number)
            odd_numbers += 0
        
    if even_numbers == 1:
        return even[0]
    else:
        return odd[0]
    
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
print(find_outlier([2, 4, 6, 8, 10, 3]))

