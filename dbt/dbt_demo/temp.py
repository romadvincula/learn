from operator import itemgetter

x = [
 ['4', '21', '1', '14', '2008-10-24 15:42:58'], 
 ['3', '22', '4', '2somename', '2008-10-24 15:22:03'], 
 ['5', '21', '3', '19', '2008-10-24 15:45:45'], 
 ['6', '21', '1', '1somename', '2008-10-24 15:45:49'], 
 ['7', '22', '3', '2somename', '2008-10-24 15:45:51']
]

print("Before sorting:")
for i in x:
    print(i)

x.sort(key=itemgetter(1))

print("After sorting:")
for i in x:
    print(i)
