def namelist(names):
    #your code here
    new_string = ""
    formatter = []

    if len(names) == 0:
        return ""
    
    for dictionary in names:
        for label, name in dictionary.items():
            if label == "name":
                formatter.append(name)

    if len(names) == 1:
        new_string = formatter[0]
    else:
        new_string = ", ".join(formatter[:-1]) + " & " + formatter[-1]
    
    return new_string

print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]))
print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]))
print(namelist([{'name': 'Bart'},{'name': 'Lisa'}]))
print(namelist([{'name': 'Bart'}]))
print(namelist([]))
