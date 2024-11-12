prime=[2,3]

def isprime(n):
    for p in prime:
        if n%p==0:
           return False
    return True

def nextprime():
    candidate=prime[-1]
    while True:
        candidate+=1
        if isprime(candidate):
            prime.append(candidate)
            break
    #return(candidate)
    for _ in range(30):
    nextprime()
print(prime)