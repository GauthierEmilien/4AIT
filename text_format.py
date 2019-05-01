from sentences import CONJUNCTION, NEGATION
import unidecode
import string


# format user entry (unaccented, no punctuation, lowercase)
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


# prend une liste a N dimension et la retourne en liste a une seule dimension
def flattenList(ndlist: list, outputList: list):
    for elem in ndlist:
        if isinstance(elem, list):
            outputList = flattenList(elem, outputList)
        else:
            outputList.append(elem)
    return outputList


# check if negation is in sentence
def checkNegation(text: [str]):
    for neg in NEGATION:
        if neg in text:
            return False
    return True
