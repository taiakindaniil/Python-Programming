numbers = list(input().split(","))

sorted_nums = {
    "natural": [],
    "integer": [],
    "rational": [],
    "real": [],
    "comp": [],
    "even": [],
    "odd": [],
    "prime": []
}

def to_int(num):
    try:
        if "/" in str(num):
            split_num = str(num).split("/")
            if float(split_num[0]) / float(split_num[1]) == 1:
                return float(split_num[0]) / float(split_num[1])

        if float(num).is_integer():
            return int(num)
        return None
    except:
        return None

def is_complex(num):
    if "j" in num:
        sorted_nums["comp"].append(num)

def is_even_odd(num):
    if to_int(num):
        sorted_nums["even"].append(num) if to_int(num) % 2 == 0 else sorted_nums["odd"].append(num)

def is_natural(num):
    n = to_int(num)
    if n != None and n > 0:
        sorted_nums["natural"].append(num)

def is_rational(num):
    if "/" in num or "." in num or num == "0":
        sorted_nums["rational"].append(num)

def is_real(num):
    if "j" not in num:
        sorted_nums["real"].append(num)

def is_prime(num):
    n = to_int(num)
    if n is None:
        return False
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while(i * i <= n) :
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6
    return True

for num in numbers:
    is_natural(num)

    if to_int(num):
        sorted_nums["integer"].append(num)

    is_even_odd(num)
    is_complex(num)
    is_rational(num)
    is_real(num)

    if is_prime(num):
        sorted_nums["prime"].append(num)

for key, value in sorted_nums.items():
    print(f"{key}:", ", ".join(value))