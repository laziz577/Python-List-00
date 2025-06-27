nums = [1,5,2,4,2,2,3]
kup_son = nums[2]
kup_soni = nums.count(kup_son)

for son in nums:
    takror_son = nums.count(son)
if takror_son > kup_soni:
    kup_son = son
    kup_soni = takror_son
print("takrorlangan son:",kup_son)
