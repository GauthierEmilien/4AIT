from sentences import RULES, TAGS, NEGATION, CONJUNCTION
from numpy import array
import unidecode
import string

memory = {}


def main():
    userTalk()


def userTalk():
    userText: str = ''
    while userText != 'quitter' and len(memory) < 5:
        if (len(memory) >= 5):
            print('other function')

        userText = str(input("Entrez une phrase : "))
        formattedText = formatText(userText)
        sentences = array(detectMultipleConjunction(formattedText)).ravel().tolist()
        detectRule(sentences)


# format user entry (unaccented, no punctuation)
def formatText(text: str):
    unaccentedStr = ' '.join(unidecode.unidecode(text).split("'"))
    formattedStr = unaccentedStr.translate(
        str.maketrans('', '', string.punctuation)).lower()
    return formattedStr


# detect conjunction in user entry and divide it in multiple sub-sentences
def detectMultipleConjunction(text: str):
    for conj in CONJUNCTION:
        splitted = text.split(conj)
        if (len(splitted) > 1):
            for i in range(len(splitted)):
                splitted[i] = detectMultipleConjunction(splitted[i])
            return splitted
    return splitted


def detectRule(sentences: [str]):
    # first way
    # for word in text.split(' '):
    #     print('word => ', word)
    #     for tag, value in TAGS.items():

    #         # TODO add REGEX here
    #         if (value == word):
    #             memorize(tag, True)

    # second way (works better)
    for sentence in sentences:
        neg = checkNegation(sentence.split(' '))
        for key, value in TAGS.items():
            if (value in sentence):
                memorize(key, neg)


# check if negation is in sentence
def checkNegation(text: list):
    for neg in NEGATION:
        if neg in text:
            return False
    return True


# add a tag to global memory
def memorize(tag: str, result: str):
    global memory
    memory[tag] = result
    print(len(memory), memory)


main()
