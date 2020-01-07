length=int(input("Input a number: "))

inputs=[]

for _ in range(0,length):
    num=input("Input a number: ")
    inputs.append(int(num))

print("Largest value:",max(inputs))
print("Smallest value:",min(inputs))
print("Average of values:",(sum(inputs)/len(inputs)))


def count_characters(string,character):
    count=0
    for current in string:
        if current==character:
            count+=1
    print("The character appears",count,"time(s)!")

string=input("Provide a string: ")
character=input("Give a character to search for: ")

count_characters(string,character)