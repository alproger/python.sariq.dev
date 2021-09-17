nums = list(range(120, 1200,2)) # 120 dan 1200 gacha juft sonlar
#print(nums)

sums = sum(nums) # ro'yhatdagi barcha sonlar yeg'indisi
print(sums)

result = max(nums) - min(nums) # ro'yhatdagi max va min ayirmasi
print(result)

lenght = len(nums) # ro'yhat uzunligi
print(lenght)

first_20 = nums[:20] # ro'yhatdagi birinchi 20ta element
print(first_20)

middle_20 = nums[ (len(nums)//2) - 10 : (len(nums)//2) + 10  ] # ro'yhatdagi o'rtasidagi 20ta element 
print(middle_20)

over_20 = nums[len(nums)-20:] # ro'yhatdagi oxirgi 20ta element 
print(over_20)