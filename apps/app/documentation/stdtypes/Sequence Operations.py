print("gg" in "eggs")
lists = [[]] * 3
print(lists)

lists[0].append(3)
lists[1].append(4)
# error
# lists[1][0].append(5)
print(lists)
print("""What has happened is that [[]] is a one-element list containing 
an empty list, so all three elements of [[]] * 3 are references 
to this single empty list. Modifying any of the elements of lists 
modifies this single list. You can create a list of different lists 
this way:""")
lists = [[] for i in range(3)]
lists[0].append(3)
lists[1].append(5)
lists[2].append(7)
print(lists)
