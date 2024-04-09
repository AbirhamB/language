def translator(phrase):
    translations=''
    for letter in phrase:
        if letter.lower() in 'eioua':
            if letter.isupper():
                translations+='G'
            else:
                translations+='g'
        else:
            translations+=letter
    return translations
print(translator(input('Enter the phrase here:')))
