import requests


def is_valid_number(number_str: str) -> bool:
    try:
        _ = float(number_str)
        return True
    except ValueError as e:
        print(f"The number given {number_str} is not a valid integer {e}")
    return False

def cast_number(number_str: str) -> int:
    try:
        return int(number_str)
    except ValueError:
        return float(number_str)

def is_prime(n: str) -> bool:
    """Check if a number is prime."""
    try:
        n=int(n)
    except ValueError:
        return False
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def sum_digit(number_str: str) -> str:
    try:
        if int(number_str)  < 0:
            number_str = number_str[1:]
        result = sum([int(number) for number in number_str])
        result=int(result)
        return result

    except ValueError: 
        return 1


def is_amstrong_number(number_str: str) -> bool:
    try:
        n = int(number_str) 
        if n == 0 or n<0:
            return False
    except ValueError:
        return False
    num_digits = len(number_str)
    result_str = []
    is_amstrong = False
    temp = []
    for number in number_str:
        temp.append(int(number) ** num_digits)
        result_str.append(f"{number}^{num_digits}")

    result = sum(temp)
    is_amstrong = result == int(number_str)

    result_str = " + ".join(result_str)
    if is_amstrong:
        result_str = f"{number_str} is an Armstrong number because " + result_str
    else:
        result_str = f"{number_str} is not an Armstrong number because " + result_str
    result_str += f" = {result}"
    return is_amstrong



def get_fun_fact(n):
    try:
        api_endpoint_str= f'http://numbersapi.com/{n}?json'
        print('Here is it', api_endpoint_str)
        response = requests.get(api_endpoint_str)
        return response.json().get('text', 'No fun fact available.')
    except Exception as e:
        return "Fun facts are only available for integers."

def is_even(n: str) -> bool:
    try:
        n = int(n) 
    except ValueError:
        return False
    return n % 2 == 0 

def is_odd(n: str) -> bool:
    try:
        n = int(n) 
    except ValueError:
        return False
    if n % 2 == 0:
        return False
    return True 

def get_number_properties(number_str: str):
    properties = []
    if is_odd(number_str):
        properties.append('odd')
    elif is_even(number_str):
        properties.append('even')
    if is_amstrong_number(number_str):
        properties.append('armstrong')
    return properties

def is_perfect(n: str) -> str:
    try:
        n = int(n) 
        if n == 0 or n<0:
            return False
    except ValueError:
        return False
    
    divisors = [i for i in range(1, n) if n % i == 0]
    return True if sum(divisors) == n else False



#print(is_even(2) == True)
#print(is_odd(3) == True)

# print(get_fun_fact(1))
#print(get_number_properties("371"))