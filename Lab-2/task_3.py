import random

def rand_table(n=10):
    return [[random.randint(1, 30) for _ in range(n)] for _ in range(n)]

def M(X, n):
    p = 1/n
    return p*sum(X)

def D(X, n):
    p = 1/n
    result = 0
    for a in X:
        result += (a - M(X, n))**2
    return p*result

if __name__ == "__main__":
    table = rand_table()
    for i, col in enumerate(table):
        print("–––––––––––––––––––––––––––––––––––––")
        print(f"Column {i}\n")
        print("Expected value: ", M(col, len(col)))
        print("Variance: ", D(col, len(col)))
        print("–––––––––––––––––––––––––––––––––––––")