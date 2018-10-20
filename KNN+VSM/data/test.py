from textblob import TextBlob, Word

if __name__ == '__main__':

    str = "time is five 86sa"
    Text =TextBlob(str)
    # word = ['as','teachers']
    print(Text.words)
    for word in Text.words:
        word = word.correct()
        # print(word)
        word =word.singularize()
        word =Word(word).lemmatize()
        word =Word(word).lemmatize("v")

        # print(Word(word).spellcheck())
        # print(Word(word).definitions)
