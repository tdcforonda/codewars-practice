def likes(names):
    # your code here
    new_names = []
    new_string = ""
    if names == []:
        return "no one likes this"
    
    for name in names:
        if len(new_names) < 3:
            if name == names[-1] and name != names[0]:
                name = "and " + name
            new_names.append(name)

    if len(new_names) > 2:
        new_string = ", ".join(new_names[:2]) + " " + new_names[-1]
    else:
        new_string = " ".join(new_names)

    if len(names) == 1:
        return new_string + " likes this"
    elif len(names) <= 3:
        return new_string + " like this"
    elif len(names) > 3:
        names_exceed = ", ".join(names[:2])
        return names_exceed + " and {} others like this".format(len(names[2:]))

print(likes([]))
print(likes(['Peter']))
print(likes(['Jacob', 'Alex']))
print(likes(['Max', 'John', 'Mark']))
print(likes(['Alex', 'Jacob', 'Mark', 'Max']))
