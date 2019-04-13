
# remove
nums = [1,2,3,4]
nums.remove(3)
print(nums)
# pop
item = nums.pop()
print(item)
print(nums)
# pop with index
nums = [1,2,3,4,5]
item = nums.pop(2)
print(item)
print(nums)
# extend
nums.extend([9,8,7])
print(nums)
# insert
nums.insert(0,-5)
print(nums)
nums.insert(3,"qqq www eee")
print(nums)
print(nums[3])
# help
# help(list)