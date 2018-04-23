print("# a = [] ===========================>")
a = []
lst = [2, -3, 0, 4, -1]  # Assign the list
print(lst);
lst[0] = 5;
print(lst[1]);
print([10, 20, 80][1])
print("# print(len([2, 4, 6, 8])) ===========================>")
print(len([2, 4, 6, 8]))
a = [10, 20, 30]
print(len(a))
print("# nums = [2, 4, 6, 8] ===========================>")
nums = [2, 4, 6, 8]
# Print last element to first (zero index) element
for i in range(len(nums) - 1, -1, -1):
    print(nums[i])
