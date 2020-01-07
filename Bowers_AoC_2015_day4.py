import hashlib
code="yzbqklnj"
number=0
while True:
    new_code=str(code)+str(number)
    encoded=new_code.encode('UTF-8')
    hashed=hashlib.md5(encoded)
    hexed=hashed.hexdigest()
    if number%1000000==0:print(number)
    if hexed[:6]=="000000":
        print(number)
        break
    number+=1