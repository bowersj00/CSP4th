infile=open('leaders.txt','r')
leaders=infile.readlines()


#iterable[start_index:stop_index] 
#gives a substring of length start_index - stop_index

for leader in leaders:
    leader=leader.strip()
    comma_index=leader.find(',')
    name=leader[:comma_index]
    score=leader[comma_index+1:]
    print("Name:", name, 'Score:', score)