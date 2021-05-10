def digital_root(n):
    n_string = str(n)
    n_list = []
    n_sum = 0
    last_sum = 0

    for i in n_string:
        i = int(i)
        n_list.append(i)

    for j in n_list:
        n_sum += j

    while len(str(n_sum)) > 1:
        last_sum = 0
        n_list.clear()
        for k in str(n_sum):
            n_list.append(int(k))
        for l in n_list:
            last_sum += l
        
        n_sum = last_sum
    
    return n_sum
            
print(digital_root(493193)) #should print 2
print(digital_root(16)) #should print 7
print(digital_root(942)) #should print 6
print(digital_root(132189)) #should print 6

