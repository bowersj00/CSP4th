alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def shifter(start_string, shift):
    new_string=""
    for character in start_string:
        if character.isalpha(): 
            new_string=new_string+(alphabet[(alphabet.index(character)+shift)%26])
        else:
            new_string=new_string+character
    print(new_string)

is_active=True

while is_active:
    start_string=str(input("Enter the string you wish to change:\n"))
    which=input("Would you like to encode (e), decode (d), or brute force (b)?\n")

    if which=="e":
        shift=int(input("How many letters to shift by? (Enter as Number)\n"))
        print("Your output is:")
        shifter(start_string,shift)
    elif which=="d":
        shift=int(input("How many letters was it shifted by?\n"))
        print("Your output is:")
        shifter(start_string,26-shift)
    elif which=="b":
        print("Cipher possibilities are:\n")
        for i in range(1,26):
            shifter(start_string,i)
    again=input("would you like to do another? (y or n)\n")
    if again=="n":
        is_active=False