empty_list = []
print(empty_list) 

my_list = [1, 2, 3, 4, 5, 6]
print(my_list) 

length_of_list = len(my_list)
print(length_of_list) 


first_item = my_list[0]
middle_item = my_list[len(my_list) // 2]
last_item = my_list[-1]
print(first_item, middle_item, last_item)  


mixed_data_types = ["Juan", 19, 163, "Single", "123 Main St"]
print(mixed_data_types)  


it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

print(it_companies) 

print(len(it_companies)) 

first_company = it_companies[0]
middle_company = it_companies[len(it_companies) // 2]
last_company = it_companies[-1]
print(first_company, middle_company, last_company)  

it_companies[0] = "Meta" 
print(it_companies) 


it_companies.append("Twitter")
print(it_companies)  

it_companies.insert(len(it_companies) // 2, "LinkedIn")
print(it_companies)  
for i in range(len(it_companies)):
    if it_companies[i] != "IBM":
        it_companies[i] = it_companies[i].upper()
print(it_companies)  

joined_companies = '#;  '.join(it_companies)
print(joined_companies) 

company_to_check = "Google"
print(company_to_check in it_companies) 


it_companies.sort()
print(it_companies) 


it_companies.reverse()
print(it_companies) 

first_three_companies = it_companies[:3]
print(first_three_companies) 

last_three_companies = it_companies[-3:]
print(last_three_companies)  

middle_index = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    middle_companies = it_companies[middle_index - 1:middle_index + 1] 
else:
    middle_companies = it_companies[middle_index:middle_index + 1] 
print(middle_companies) 
it_companies.pop(0)
print(it_companies)  

middle_index = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    it_companies.pop(middle_index - 1)  
    it_companies.pop(middle_index - 1) 
else:
    it_companies.pop(middle_index)  
print(it_companies)

it_companies.pop()
print(it_companies)

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

it_companies.clear()  
print(it_companies) 

del it_companies  


front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

full_stack = front_end + back_end
print(full_stack) 

full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Python') + 1, 'SQL')
print(full_stack)
