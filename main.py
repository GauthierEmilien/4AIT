from sentences import RULES, TAGS, NEGATION, CONJUNCTION
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
        detectMultipleConjunction(formattedText)
        # detectRule(formatText(userText))


def formatText(text: str):
    unaccentedStr = ' '.join(unidecode.unidecode(text).split("'"))
    formattedStr = unaccentedStr.translate(
        str.maketrans('', '', string.punctuation)).lower()
    return formattedStr


def detectMultipleConjunction(text: [str]):
    hasConj = False
    for word in text[0].split():
        if ' ' + word + ' ' in CONJUNCTION:
            hasConj = True
    if hasConj:
        return text
    
    # for conj in CONJUNCTION:
    #     splitted = text.split(conj)
    #     for sentence in splitted:
    #         detectMultipleConjunction(sentence)
        



# check if conjunction is in sentence
# def checkConjunction(sentences: [str], conj: str):
#     for sentence in sentences:
#         checkConjunction(sentence.split(conj), conj)


def detectRule(text: str):
    # first way
    # for word in text.split(' '):
    #     print('word => ', word)
    #     for tag, value in TAGS.items():

    #         # TODO add REGEX here
    #         if (value == word):
    #             memorize(tag, True)

    # second way (works better)
    neg = checkNegation(text.split(' '))
    for key, value in TAGS.items():
        if (value in text):
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
