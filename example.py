'''
# Написали функцию нахождения площади и попросили добавить 2 стороны для норм. работы
def square(a,b):
    return a * b # достаем полученный рехультат из ф-и

save_result = square(2,3) # Сохраняем результат в переменной
    
#количество колонн(a)=13
#расстояние между колоннами(b)=600
#ширина колонны(c)=80
#расст от первой до последней(x)=? 
def task(a=13,b=600,c=80):
    print(a*b+c)  
    return(a,b,c)
    task() 


string = 'КонфАтти'

result = string.replace('А', "е")

print(string)

print(result)
    
#print(result[::-1])       

print(result[0])    
        
print(result[-1])
print(result[5])    

print(result[0:6] + 'a')
print(result[0:4]+'a')
print(result[3:6])
print(result[3:6] + 'a') ''' 

# слова
string = 'дезинформация'
text = 'text'
number = 5
#raise TypeError
print(string[3:12])
print(string[3:13])
print(string[5:13])
print(string[5:9])
print(string[5:10])

print(string[4+9:13])
