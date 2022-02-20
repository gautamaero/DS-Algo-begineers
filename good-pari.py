
def goodparis(nums):
    counter=0
    if (len(nums)>1):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                #print('made loop',nums[i],nums[j])
                if nums[i]==nums[j]:
                    counter+=1

    return counter

nums= list(map(int,input().split()))

print(goodparis(nums))






