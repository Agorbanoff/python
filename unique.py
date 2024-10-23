nums = [1, 2, 3, 2, 4, 5, 3, 6, 7]
start = 0
max_len = 0
max_start = 0
seen = {}

for i in range(len(nums)):
    num = nums[i]
    if num in seen and seen[num] >= start:
        start = seen[num] + 1
    seen[num] = i
    if i - start + 1 > max_len:
        max_len = i - start + 1
        max_start = start

result = nums[max_start:max_start + max_len]
print(result)
