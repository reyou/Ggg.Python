# The statement
a = [2, 4, 6, 8]
# assigns the given list literal to the variable a. The expression
a + [1, 3, 5]
# evaluates to the list [2, 4, 6, 8, 1, 3, 5], but the statement
# does not change the list to which a refers.
# The statement
a = a + [1, 3, 5]
# actually reassigns ato the new list [2, 4, 6, 8, 1, 3, 5]. The statement
a += [10]
# updates ato be the new list [2, 4, 6, 8, 1, 3, 5, 10]. Observe that the +will concatenate two lists,
# but it cannot join a list and a non-list.
print(a)