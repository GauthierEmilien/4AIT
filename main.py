from sentences import CITIES, TAGS, NEGATION, CONJUNCTION
from text_format import formatText, checkNegation, detectMultipleConjunction, flattenList
from bot import Bot
from numpy import array

bot = Bot()


def main():
    userTalk()


def userTalk():
    userText: str = ''
    sentences: [str] = []

    while userText != 'quitter':
        bot.detectRule(sentences)
        bot.setPreferedCities()
        for city in bot.getPreferedCities():
            print(city['city']['where'])
        bot.talk(userText)

        userText = str(input("> "))
        formattedText = formatText(userText)
        sentences = flattenList(detectMultipleConjunction(formattedText), [])


main()
