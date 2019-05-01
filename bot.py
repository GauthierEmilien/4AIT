from operator import itemgetter
from random import choice
from sentences import CITIES, TAGS, SENTENCES, DESCRIPTION_WORDS
from text_format import checkNegation


class Bot:
    def __init__(self):
        self.__memory: dict = {}
        self.__preferedCities = []
        self.__hasUnderstand = False
        self.__detectedCity = ''
        self.__wantDescription = False

    def memorize(self, tag: str, result: str):
        self.__memory[tag] = result
        # print(self.__memory)

    def getPreferedCities(self):
        return self.__preferedCities

    def setPreferedCities(self):
        citiesPreferences = []
        for city in CITIES:
            preference = 0

            for tag, value in self.__memory.items():
                if TAGS[tag] in city['tags'] and value:
                    preference += 2
                elif not value and TAGS[tag] not in city['tags']:
                    preference += 1

            citiesPreferences.append(
                {'city': city, 'preference': preference})

        citiesPreferences = sorted(
            citiesPreferences, key=itemgetter('preference'), reverse=True)

        maxValue = citiesPreferences[0]['preference']
        self.__preferedCities = [citiesPreferences[0]]
        for i in range(1, len(citiesPreferences)):
            if citiesPreferences[i]['preference'] == maxValue:
                self.__preferedCities.append(citiesPreferences[i])

    def detectRule(self, sentences: [str]):
        # first way
        # for word in text.split(' '):
        #     print('word => ', word)
        #     for tag, value in TAGS.items():

        #         # TODO add REGEX here
        #         if (value == word):
        #             memorize(tag, True)

        # second way (works better)
        self.__hasUnderstand = False
        for sentence in sentences:
            neg = checkNegation(sentence.split(' '))
            for key, value in TAGS.items():
                if (value in sentence):
                    self.memorize(key, neg)
                    self.__hasUnderstand = True

            if not self.__hasUnderstand:
                self.__detectedCity = ''
                self.__wantDescription = False
                for city in self.__preferedCities:
                    if city['city']['where'] in sentence:
                        self.__detectedCity = city['city']['where']

                for word in DESCRIPTION_WORDS:
                    if word in sentence and self.__detectedCity:
                        self.__wantDescription = True

    def canSuggest(self):
        if len(self.__preferedCities) <= 2:
            return True
        return False

    def talk(self, userText: str):
        if not userText:
            print('BOT>', SENTENCES['bonjour'], sep='')
        elif self.__wantDescription:
            for city in self.__preferedCities:
                if self.__detectedCity == city['city']['where']:
                    print('BOT>', city['city']['description'], sep='')
        elif not self.__hasUnderstand:
            print('BOT>', SENTENCES['not_understand'], sep='')
        elif self.canSuggest():
            print('BOT>Je peux vous proposer', end=' ')
            for index, city in enumerate(self.__preferedCities):
                print(city['city']['where'].capitalize(), end=' ')
                if len(self.__preferedCities) > 1 and index < len(self.__preferedCities) - 1:
                    print('ou', end=' ')
            print()
        else:
            print('BOT>', choice(SENTENCES['react_to_proposition']), sep='')
