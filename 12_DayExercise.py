import random
import string

def random_user_id():
    """Generates a six character random user ID."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

print(random_user_id())  

def user_id_gen_by_user():
    """Generates user IDs based on user input for length and quantity."""
    length = int(input("Enter the number of characters for the user ID: "))
    quantity = int(input("Enter the number of user IDs to generate: "))
    
    user_ids = []
    for _ in range(quantity):
        user_id = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        user_ids.append(user_id)
    
    return user_ids


print(user_id_gen_by_user())  

def rgb_color_gen():
    """Generates a random RGB color."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"

print(rgb_color_gen())

def list_of_hexa_colors(n):
    """Generates a list of hexadecimal colors."""
    hex_colors = []
    for _ in range(n):
        color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
        hex_colors.append(color)
    return hex_colors


print(list_of_hexa_colors(5)) 

def list_of_rgb_colors(n):
    """Generates a list of RGB colors."""
    rgb_colors = []
    for _ in range(n):
        rgb_colors.append(rgb_color_gen())
    return rgb_colors

print(list_of_rgb_colors(5))  

def generate_colors(color_type, n):
    """Generates a specified number of colors in either hex or RGB format."""
    if color_type == 'hexa':
        return list_of_hexa_colors(n)
    elif color_type == 'rgb':
        return list_of_rgb_colors(n)
    else:
        return "Invalid color type. Please choose 'hexa' or 'rgb'."


print(generate_colors('hexa', 3)) 
print(generate_colors('rgb', 3))  

def shuffle_list(lst):
    """Shuffles a list and returns it."""
    random.shuffle(lst)
    return lst


my_list = [1, 2, 3, 4, 5]
print(shuffle_list(my_list)) 

def unique_random_numbers():
    """Returns an array of seven unique random numbers in the range of 0-9."""
    return random.sample(range(10), 7)

