from sentences import SENTENCES
from text_format import formatText, checkNegation, detectMultipleConjunction, flattenList
from bot import Bot
from numpy import array
from random import choice
import re

bot = Bot()


def main():
    # print(re.findall(r'\{(.[^\{])*\}', SENTENCES['bonjour']))
    # print(choice(SENTENCES['react_to_proposition']))
    # print(SENTENCES['bonjour'].format('emilien', ''))
    userTalk()


def userTalk():
    userText: str = ''
    sentences: [str] = []

    while userText != 'quitter':
        hasUnderstand = bot.detectRule(sentences)
        bot.setPreferedCities()
        bot.talk(userText, hasUnderstand)

        userText = str(input("> "))
        formattedText = formatText(userText)
        sentences = flattenList(detectMultipleConjunction(formattedText), [])


main()
