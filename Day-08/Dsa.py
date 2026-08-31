#Two sum
nums = [2, 7, 11, 15]
target = 13
dit={}
for i ,n in enumerate(nums):
    required=target-n
    if required in dit:
        print(f'{dit[required]},{i}')
    dit[n]=i


    