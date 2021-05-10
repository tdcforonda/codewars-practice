def filter_list(l):
    filtered_list = []
    for item in l:
        x = item
        if isinstance(item,int):
            filtered_list.append(item)
    return filtered_list

print(filter_list([1,2,'a','b']))
print(filter_list([1,'a','b',0,15]))
print(filter_list([1,2,'aasf','1','123',123]))
