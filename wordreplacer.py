word=input('Write the word you want to change: ')
new_word=input('Write the word you want to change it with: ')

with open(f'test.txt','r') as f:
    file=f.read()
file=file.replace(word,new_word)

with open(f'test.txt','w') as f:
    f.write(file)