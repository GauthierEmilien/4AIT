from operator import itemgetter
from sentences import CITIES, TAGS
from text_format import checkNegation


class Bot:
    def __init__(self):
        self.__memory: dict = {}
        self.__citiesPreferences = []

    def memorize(self, tag: str, result: str):
        self.__memory[tag] = result
        print(self.__memory)

    def getPreferedCities(self):
        maxValue = self.__citiesPreferences[0]['preference']
        preferedCities = [self.__citiesPreferences[0]]
        for i in range(1, len(self.__citiesPreferences)):
            if self.__citiesPreferences[i]['preference'] == maxValue:
                preferedCities.append(self.__citiesPreferences[i])
        return preferedCities

    def setPreferedCities(self):
        self.__citiesPreferences = []
        for city in CITIES:
            preference = 0

            for tag, value in self.__memory.items():
                if TAGS[tag] in city['tags'] and value:
                    preference += 2
                elif not value and TAGS[tag] not in city['tags']:
                    preference += 1

            self.__citiesPreferences.append(
                {'city': city, 'preference': preference})

        self.__citiesPreferences = sorted(
            self.__citiesPreferences, key=itemgetter('preference'), reverse=True)

    def detectRule(self, sentences: [str]):
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
                    self.memorize(key, neg)
