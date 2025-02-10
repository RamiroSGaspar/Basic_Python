n = int(input("Ingresa un numero: "))

if n < 2:
    print(f"{n} no es un numero primo. ")
else:
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            print(f"{n} no es un numero primo. ")
            break
    else:
        print(f"{n} es un numero primo. ")
        