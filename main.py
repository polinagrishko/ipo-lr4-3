fib1=1
fib2=1
n=input("номер элемента ряда фибоначчи:")
n=int(n)
i=0
while i < n-2:
    fib_sum=fib1+fib2
    fib1=fib2
    fib2=fib_sum
    i=i+1
    print("значение элемента:",fib2)
