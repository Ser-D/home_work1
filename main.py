

message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""

for ch in message:

    if  ord(ch) >= 65 and ord(ch) <= 90:
       ch_new = chr((ord(ch) - 65 + offset) % 26 + 65)
    elif ord(ch) >= 97 and ord(ch) <= 122:
        ch_new = chr((ord(ch) - 97 + offset) % 26 + 97)
    else:
         ch_new = ch
    encoded_message += ch_new
    

print(encoded_message)



    
    


