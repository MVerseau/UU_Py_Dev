
def is_prime(f):
    def wrapper(*args,**kwargs):
        num=f(*args)
        for n in range(2, int(num**0.5)+1):
            if num%n==0:
                return f'Составное\n{num}'
        return f'Простое\n{num}'
    return wrapper

@is_prime
def sum_three(a,b,c):
    return a+b+c

result = sum_three(2, 3, 6)
print(result)