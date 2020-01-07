infile=open("Bowers_AoC_2015_day2_Inputs.txt","r")
lines=infile.readlines()
infile.close()
total_count=0
for line in lines:
    line=line.strip()
    first_x=line.find("x")
    second_x=line.rfind("x")
    length=int(line[:first_x])
    width=int(line[first_x+1:second_x])
    height=int(line[second_x+1:])

    face1p=((2*length)+(2*width))
    face2p=((2*length)+(2*height))
    face3p=((2*width)+(2*height))

    bow=length*width*height

    if face1p<=face2p and face1p<=face3p:
        ribbon=(face1p)
    elif face2p<=face1p and face2p<=face3p:
        ribbon=(face2p)
    elif face3p<=face1p and face3p<=face2p:
        ribbon=(face3p)

    total_count+=(ribbon+bow)
print(total_count)