#Write your code below this line 👇
def prime_checker(number):
    is_Prime = True
    if number % 2 == 0 and number != 2:
        print("It's not a prime number.")
        exit(1)
    else:
        for i in range(2, number - 1):
            if number % i == 0:
                is_Prime = False
       
    if is_Prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
        
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
