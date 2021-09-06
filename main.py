#Write your code below this line 👇

def prime_checker(number):
  count = 0
  for num in range(1,number):
    if number%num == 0:
      count+=1

  if count > 2:
    print("The number is not prime")
  else:
    print("The number is prime")
  



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



