from sentences import CITIES, TAGS, NEGATION, CONJUNCTION
from text_format import formatText, checkNegation, detectMultipleConjunction
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
        # botTalk()

        userText = str(input("> "))
        formattedText = formatText(userText)
        sentences = array(detectMultipleConjunction(
            formattedText)).ravel().tolist()


main()
