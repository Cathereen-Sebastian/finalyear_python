n=int(input("enter the limit :"))
if n < 2 :
    print("not prime number")
for num in range(2,n+1):
    is_prime = True
    for i in range(2,num):
        if num%i ==0:
            is_prime = False
            break
    if is_prime:
        print(num)
