data = '''But soft what light through yonder window breaks
It is the east and Juliet is the sun
Arise fair sun and kill the envious moon
Who is already sick and pale with grief'''

lines = data.split('\n')

unique_words = []

for line in lines:
    words = line.split()
    
    for word in words:
        if word not in unique_words:
            unique_words.append(word)

unique_words.sort()

print(unique_words)