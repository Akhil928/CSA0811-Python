def permutations(str_val):
    if len(str_val) == 0:
        return ['']
    pre = permutations(str_val[1:len(str_val)])
    next = []
    for i in range(0,len(pre)):
        for j in range(0,len(str_val)):
            new_str_val = pre[i][0:j]+str_val[0]+pre[i][j:len(str_val)-1]
            if new_str_val not in next:
                next.append(new_str_val)
    return next
 
str_val = input("Enter the Numbers :")
print(permutations(str_val))
