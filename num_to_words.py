## THIS IS A PROGRAM FOR CONVERTING A NUMBER INTO WORDS ##

numbers = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]

tens = ["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Ninteen"]

nty = ["","","Twenty","Thirty","Fourty","Fifty","Sixty","Seventy","Eighty","Ninty"]

n = int(input("ENTER THE NUMBER:   "))
with open("numbers.txt","a") as file:
    file.write(str(n) + "\t")
if n > 99999:
    print("CAN'T SOLVE MORE THEN FIVE DIGITS...") 
else:
    num = ""
    if n == 0:
        num += "Zero"
    if n < 0:
        num += "Minus "
        n = -n
    d = [0,0,0,0,0]
    i = 0
    while n > 0:
        d[i] = n%10
        i += 1
        n = n // 10
    if d[4] != 0:
        if d[4] == 1:
            num += tens[d[3]] + " Thousand "
        else:
            num += nty[d[4]] +" "+ numbers[d[3]] + " Thousand "
    else:
        if d[3] != 0:
            num += numbers[d[3]] + " Thousand "
    if d[2] != 0:
        num += numbers[d[2]] +" Hundred "
    if d[1] != 0:
        if d[1] == 1:
            num += tens[d[0]]
        else:
            num += nty[d[1]] +" "+ numbers[d[0]]
    else:
        if d[0] != 0:
            num += numbers[d[0]] 
    with open("numbers.txt","a") as file:
        file.write(num + "\n")
    print(str(num))            

