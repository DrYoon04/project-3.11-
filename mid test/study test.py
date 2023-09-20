word_to_count = '삼척시'
count = 0

with open('wow.txt','r',encoding = 'utf-8') as file:
    content = file.read()
    words = content.split()
    for word in words:
        if word.find(word_to_count):
            print(word)
            count += 1
print(f"'{word_to_count}' 단어의 빈도 : {count}")