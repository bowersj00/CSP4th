infile=open("Bowers_AoC_2015_day5_inputs.txt","r")
lines=infile.readlines()
infile.close()

nice=0

for line in lines:
    is_nice=False
    has_single_repeat=False
    index=0
    for character in line:
        if index<len(line)-2:
            if character == line[index+2]:
                has_single_repeat=True
        index+=1
    if has_single_repeat and is_nice==False:
        nice+=1

print(nice)