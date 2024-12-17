# A  = {1,5,7}
# B = {2,4,6,7}

# a_union_b = A.union(B)
# a_union_b_without_function = A | B
# print(a_union_b_without_function)

set1 = set()
set2 = set()
for i in range (5):
    set1.add(i)
    for i in range (3,9):
        set2.add(i)
        
        # interesection using
        set3 = set1.intersection(set2)
        print("intersection using intersection ()funcation")
        print(set3)
        
        set4= set1&set2
        print("\nintersection using '&' operator")
        print(set4 )