# 1)

a =  [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
new_a = []
def flatten(data):
    for l in data:
        if type(l) == list:
            flatten(l)
        else :
            new_a.append(l)
flatten(a)
print(new_a)

# 2)

a = [[1, 2], [3, 4], [5, 6, 7]]
new = []

for i in reversed(a) :
    if type(i) == list :
        new.append(i[:: -1])
        
    else :
        print("not true")

print(new)