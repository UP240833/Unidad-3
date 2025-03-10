string1 = 'Thirty'
string2 = 'Days'
string3 = 'Of'
string4 = 'Python'
result1 = string1 + ' ' + string2 + ' ' + string3 + ' ' + string4
print(result1) 

string5 = 'Coding'
string6 = 'For'
string7 = 'All'
result2 = string5 + ' ' + string6 + ' ' + string7
print(result2) 

company = "Coding For All"
print(company) 


print(len(company))  

print(company.upper()) 
print(company.lower())  


print(company.capitalize()) 
print(company.title())       
print(company.swapcase())   


first_word_cut = company[7:] 
print(first_word_cut) 

print('Coding' in company)  


new_company = company.replace('Coding', 'Python')
print(new_company)  

new_string = 'Python for Everyone'
new_string = new_string.replace('Everyone', 'All')
print(new_string) 

split_string = company.split() 
print(split_string) 

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
split_companies = companies.split(', ')
print(split_companies)  

print(company[0]) 

print(len(company) - 1)  

print(company[10]) 


acronym1 = 'Python For Everyone'.replace(' ', '').upper()  
acronym2 = 'Coding For All'.replace(' ', '').upper()  
print(acronym1, acronym2)  

print(company.index('C')) 

print(company.index('F'))

print(company.rfind('l'))  

sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because')) 
print(sentence.rindex('because'))  


sliced_sentence = sentence[39:63]  
print(sliced_sentence)

print(company.startswith('Coding'))  
print(company.endswith('coding'))     


spaced_string = '   Coding For All      '
print(spaced_string.strip()) 

print('30DaysOfPython'.isidentifier())  
print('thirty_days_of_python'.isidentifier()) 

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_libraries = ' # '.join(libraries)
print(joined_libraries)  
sentence1 = "I am enjoying this challenge."

sentence2 = "I just wonder what is next."
print(sentence1 + '\n' + sentence2)  

print("Name\tAge\tCountry\tCity")
print("AldoF\t18\tMexico\tAguascalientes")

radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

print(f"8 + 6 = {8 + 6}")
print(f"8 - 6 = {8 - 6}")
print(f"8 * 6 = {8 * 6}")
print(f"8 / 6 = {8 / 6:.2f}")
print(f"8 % 6 = {8 % 6}")
print(f"8 // 6 = {8 // 6}")
print(f"8 ** 6 = {8 ** 6}")