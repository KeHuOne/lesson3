#Скачайте файл по ссылке
#Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
#Подсчитайте количество слов в тексте
#Замените точки в тексте на восклицательные знаки
#Сохраните результат в файл referat2.txt

with open('referat.txt', 'r', encoding='utf-8') as text:
    content = text.read()
    print(f'Длина получившейся строки {len(content)}.')

    length = content.split()
    print(f'Количество слов {len(length)}.')
    
    text.close()

with open('referat2.txt', 'w',encoding='utf-8') as text:
    text.write(content.replace('.', '!'))

    text.close()


