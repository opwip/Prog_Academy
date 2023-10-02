def remove_bad_words(text: str, bad_words: list):
    for item in bad_words:
        text = text.replace(item, "*")
    return text


def words_count(sentence: str):
    punctuations = ',.!?'
    for item in punctuations:
        sentence = sentence.replace(item, ' ')
    return len(sentence.split())


while (ans := input('text=').lower()) != 'exit':
    print(words_count(ans))

very_bad_words = ["bad", "ugly"]
print(remove_bad_words(input(), very_bad_words))
