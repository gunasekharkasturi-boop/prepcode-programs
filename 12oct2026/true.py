number = int(input("enter the number:"))
starting = 2
its_prime = True
while starting < number:
    if number % starting == 0:
        is_prime = False
        starting += 1
print(is_prime)
