from bot import Bot
from text_format import formatText, detectMultipleConjunction, flattenList

bot = Bot()


def main():
    # print(re.findall(r'\{(.[^\{])*\}', SENTENCES['bonjour']))
    # print(SENTENCES['bonjour'].format('emilien', ''))
    userTalk()


def userTalk():
    userText: str = ''
    sentences: [str] = []

    while userText != 'quitter':
        bot.detectRule(sentences)
        bot.setPreferedCities()
        bot.talk(userText)

        userText = str(input("YOU> "))
        formattedText = formatText(userText)
        sentences = flattenList(detectMultipleConjunction(formattedText), [])


main()
