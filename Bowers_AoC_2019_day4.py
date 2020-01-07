solutions=[]
tests=[577777,556888,777789]
for password in range(265275,781584):
#for password in tests:
    str_pass=str(password)
    contains_double=False
    counts_down=False
    current=str_pass[1]
    last=str_pass[0]
    index=1
    for num in str_pass:
        if current==last:
            contains_double=True
        if current<last:
            counts_down=True
        last=current
        index+=1
        if index<len(str_pass):
            current=str_pass[index]
        else:
            break
    if contains_double and not counts_down:
        solutions.append(password)

#print(solutions)

solutions_2=[]

for solution in solutions:
    str_pass=str(solution)

    zero=0
    one=0
    two=0
    three=0
    four=0
    five=0
    six=0
    seven=0
    eight=0
    nine=0
    for digit in str_pass:
        if digit=="0":
            zero+=1
        elif digit=="1":
            one+=1
        elif digit=="2":
            two+=1
        elif digit=="3":
            three+=1
        elif digit=="4":
            four+=1
        elif digit=="5":
            five+=1
        elif digit=="6":
            six+=1
        elif digit=="7":
            seven+=1
        elif digit=="8":
            eight+=1
        elif digit=="9":
            nine+=1
    digits=[one,two,three,four,five,six,seven,eight,nine]
    if max(digits)<3 and max(digits)>1:
        solutions_2.append(solution)
    elif max(digits)>2 and 2 in digits:
        solutions_2.append(solution)

print(len(solutions_2))