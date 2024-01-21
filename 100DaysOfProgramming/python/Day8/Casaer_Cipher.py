from modules import casear_art

def caesar(text, shift, direction):
    string = ""
   
    for char in text:
        exists = False 
        for index in range(0, 26):
            if char == alphabet[index]:
                exists = True
                if direction == 'encode':
                    total = index + shift
                    
                    if total >= 26:
                        string += alphabet[total - 26]    
                    else:
                        string += alphabet[total]
                    
                elif direction == "decode":
                    total = index - shift
                    
                    if total >= 26:
                        string += alphabet[total + 26]    
                    else:
                        string += alphabet[total]
                
        if exists == False:
            string += char
    print(f"Your string is: {string}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
resume = ""
print (casear_art.logo)
should_continue = True
while should_continue == False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    caesar(text=text, direction=direction, shift=shift)
   
    resume = input("Continue? (Yes/No) ").lower()
    if resume == "no":
        should_continue = False
        print("L8s")
    