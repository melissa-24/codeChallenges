# https://www.codewars.com/kata/520b9d2ad5c005041100000f

# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

# Examples
# pigIt('Pig latin is cool'); // igPay atinlay siay oolcay
# pigIt('Hello world !');     // elloHay orldway !

# separate words from punctuation
# remove 1st letter of each word and add it to the end
# add ay to the end of each edited word


def pigIt(sentence):
    words = sentence.split()
    print('words', words)

    def makePigLatin(word):
        isPunctuation = word[-1] in ('.', ',', '!', '?', ';', ':')
        if isPunctuation:

            pigLatinWord = makePigLatin(word[:-1]) + word[-1]
            return pigLatinWord
        else:
            pigLatinWord = word[1:] + word[0] + 'ay'
            return pigLatinWord

    pigLatinizedWords = map(makePigLatin, words)

    return ' '.join(pigLatinizedWords)





print(pigIt('Hello World!'))
print(pigIt("Hello! Welcome Big Bad World!"))