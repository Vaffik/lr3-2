print("Введите 2 целых числа: ", end = "")
x = int(input()) #запрашивается 1 число с клавиатуры
y = int(input()) #запрашивается 2 число с клавиатуры
if x == y:  #проверка: если 1 == 2
    print("Числа равны")
else: #1 условие если x < y 2 условие если x > y 
    print(f"Число {x} меньше") if x < y else print(f"Число {y} меньше")