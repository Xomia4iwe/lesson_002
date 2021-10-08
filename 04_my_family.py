

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = []
my_family.append('Отец')
my_family.append('Мать')
my_family.append('Жона')
my_family.append('Швагерка')
my_family.append('Я')
print(my_family)
# список списков приблизителного роста членов вашей семьи
Dad = ['Виктор', 175]
Mom = ['Ирина', 168]
Wife = ['Ольга', 172]
Wife_brother = ['Евгения', 63]
I = ['Евгений', 180]


my_family_height = [Dad, Mom, Wife, Wife_brother, I]
print('Рост отца - ' + str(my_family_height[0][1]) + ' см')
# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
all_my_family_height = (my_family_height[0][1]+my_family_height[1][1]+my_family_height[2][1]+my_family_height[3][1]+my_family_height[4][1])
print('Общий рост моей семьи ' + str(all_my_family_height) + ' см')
#   Общий рост моей семьи - ХХ см
