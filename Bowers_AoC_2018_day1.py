infile=open('Bowers_AoC_2018_day1_inputs.txt','r')
lines=infile.readlines()
result_list=[]
current=0
found=False
while found==False:
    for line in lines:
        current+=int(line)
        if current in result_list:
            print(current)
            found=True
        else:
            result_list.append(current)
print("finished")
