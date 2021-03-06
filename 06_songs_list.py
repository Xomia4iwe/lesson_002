

# Есть список песен группы Depeche Mode со временем звучания с точносттю до долей минут

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ минут
# Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
# Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)

# TODO здесь ваш код

time = violator_songs_list[3][1] + violator_songs_list[5][1] + violator_songs_list[-1][1]
print('Три песни звучат ' + str(round(time, 3)) + ' минут')

# Есть словарь песен группы Depeche Mode
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}



# TODO здесь ваш код
time2 = violator_songs_dict['Sweetest Perfection'] + violator_songs_dict['Policy of Truth'] + violator_songs_dict['Blue Dress']
print('Общее время трех песен Sweetest Perfection, Policy of Truth и Blue Dress ' + str(round(time2, 3)) + ' минут')

time3 = violator_songs_dict['World in My Eyes'] + violator_songs_dict['Personal Jesus'] + violator_songs_dict['Halo']\
        + violator_songs_dict['Waiting for the Night'] + violator_songs_dict['Enjoy the Silence'] + violator_songs_dict['Clean']

print( 'А другие песни звучат '  + str(round(time3, 3)) + ' минут')