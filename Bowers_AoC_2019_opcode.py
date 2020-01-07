nums=[1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,5,23,1,6,23,27,1,27,5,31,2,31,10,35,2,35,6,39,1,39,5,43,2,43,9,47,1,47,6,51,1,13,51,55,2,9,55,59,1,59,13,63,1,6,63,67,2,67,10,71,1,9,71,75,2,75,6,79,1,79,5,83,1,83,5,87,2,9,87,91,2,9,91,95,1,95,10,99,1,9,99,103,2,103,6,107,2,9,107,111,1,111,5,115,2,6,115,119,1,5,119,123,1,123,2,127,1,127,9,0,99,2,0,14,0]
#nums=[1,9,10,3,2,3,11,0,99,30,40,50]
current_pos=0

while nums[current_pos]!=99:
    current=nums[current_pos]
    if current==1:
        num1=nums[nums[current_pos+1]]
        num2=nums[nums[current_pos+2]]
        new=nums[current_pos+3]
        nums.pop(new)
        nums.insert(new,(num1+num2))
        current_pos+=4
    else:
        num1=nums[nums[current_pos+1]]
        num2=nums[nums[current_pos+2]]
        new=nums[current_pos+3]
        nums.pop(new)
        nums.insert(new,(num1*num2))
        current_pos+=4

print(nums)