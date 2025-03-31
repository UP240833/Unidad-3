import math

def add_two_numbers(a, b):
    return a + b

def area_of_circle(r):
    return math.pi * r * r

def add_all_nums(*args):
    if all(isinstance(num, (int, float)) for num in args):
        return sum(args)
    else:
        return "All items must be numbers."

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def check_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    elif month in [9, 10, 11]:
        return "Autumn"
    else:
        return "Invalid month"

def calculate_slope(y2, y1, x2, x1):
    return (y2 - y1) / (x2 - x1)

def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (root1, root2)
    elif discriminant == 0:
        root = -b / (2*a)
        return (root,)
    else:
        return "No real roots"

def print_list(lst):
    for item in lst:
        print(item)

def reverse_list(arr):
    reversed_arr = []
    for item in arr:
        reversed_arr.insert(0, item)
    return reversed_arr

def capitalize_list_items(lst):
    return [item.capitalize() for item in lst]

def add_item(lst, item):
    lst.append(item)
    return lst

def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

def sum_of_numbers(n):
    return sum(range(n + 1))

def sum_of_odds(n):
    return sum(i for i in range(n + 1) if i % 2 != 0)

def sum_of_even(n):
    return sum(i for i in range(n + 1) if i % 2 == 0)

def evens_and_odds(n):
    evens = sum(1 for i in range(n + 1) if i % 2 == 0)
    odds = sum(1 for i in range(n + 1) if i % 2 != 0)
    return f"The number of evens are {evens}. The number of odds are {odds}."

def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def is_empty(param):
    return param == []

def calculate_mean(lst):
    return sum(lst) / len(lst)

def calculate_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

def calculate_mode(lst):
    return max(set(lst), key=lst.count)

def calculate_range(lst):
    return max(lst) - min(lst)

def calculate_variance(lst):
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)

def calculate_std(lst):
    return math.sqrt(calculate_variance(lst))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_items_unique(lst):
    return len(lst) == len(set(lst))

def all_items_same_type(lst):
    return all(isinstance(item, type(lst[0])) for item in lst)

def is_valid_variable(var):
    return var.isidentifier()



def most_spoken_languages():
    countries_data = {
        'countries': [
            {'name': 'China', 'languages': ['Mandarin']},
            {'name': 'India', 'languages': ['Hindi', 'English']},
            {'name': 'USA', 'languages': ['English']},
            {'name': 'Indonesia', 'languages': ['Indonesian']},
            {'name': 'Pakistan', 'languages': ['Urdu', 'English']},
            {'name': 'Brazil', 'languages': ['Portuguese']},
            {'name': 'Nigeria', 'languages': ['English', 'Hausa']},
            {'name': 'Bangladesh', 'languages': ['Bengali']},
            {'name': 'Russia', 'languages': ['Russian']},
            {'name': 'Mexico', 'languages': ['Spanish']},
            {'name': 'Philippines', 'languages': ['Filipino', 'English']},
            {'name': 'Vietnam', 'languages': ['Vietnamese']},
            {'name': 'Turkey', 'languages': ['Turkish']},
            {'name': 'Iran', 'languages': ['Persian']},
            {'name': 'Germany', 'languages': ['German']},
            {'name': 'Thailand', 'languages': ['Thai']},
            {'name': 'France', 'languages': ['French']},
            {'name': 'Italy', 'languages': ['Italian']},
            {'name': 'South Africa', 'languages': ['Afrikaans', 'English', 'Zulu', 'Xhosa']},
            {'name': 'Tanzania', 'languages': ['Swahili', 'English']},
            {'name': 'South Korea', 'languages': ['Korean']}
        ]
    }
    
    language_count = {}
    for country in countries_data['countries']:
        for language in country['languages']:
            if language in language_count:
                language_count[language] += 1
            else:
                language_count[language] = 1

    most_spoken = sorted(language_count.items(), key=lambda x: x[1], reverse=True)[:10]
    return [language for language, count in most_spoken]

def most_populated_countries():
    countries_data = {
        'countries': [
            {'name': 'China', 'population': 1400},
            {'name': 'India', 'population': 1380},
            {'name': 'USA', 'population': 331},
            {'name': 'Indonesia', 'population': 273},
            {'name': 'Pakistan', 'population': 225},
            {'name': 'Brazil', 'population': 213},
            {'name': 'Nigeria', 'population': 206},
            {'name': 'Bangladesh', 'population': 166},
            {'name': 'Russia', 'population': 146},
            {'name': 'Mexico', 'population': 126},
            {'name': 'Japan', 'population': 125},
            {'name': 'Ethiopia', 'population': 114},
            {'name': 'Philippines', 'population': 113},
            {'name': 'Egypt', 'population': 102},
            {'name': 'Vietnam', 'population': 98},
            {'name': 'DR Congo', 'population': 89},
            {'name': 'Turkey', 'population': 84},
            {'name': 'Iran', 'population': 83},
            {'name': 'Germany', 'population': 83},
            {'name': 'Thailand', 'population': 70},
            {'name': 'United Kingdom', 'population': 67}
        ]
    }
    
    most_populated = sorted(countries_data['countries'], key=lambda x: x['population'], reverse=True)[:10]
    return [(country['name'], country['population']) for country in most_populated]