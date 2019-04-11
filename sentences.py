""" ALL WHITESPACE BEFORE WORDS ARE VERY IMPORTANT, DO NOT DELETE THEM"""

TAGS = {
    'urbain': 'urbain',
    'rural': 'rural',
    'calme': 'calme',
    'soleil': 'soleil',
    'visite': 'visite',
    'archi': 'architecture',
    'paysage': 'paysages',
    'montagne': 'montagne',
    'chic': 'chic',
    'bon marche': 'bon marche',
    'prix moyen': 'prix moyen',
    'chaud': 'chaud',
    'froid': 'froid',
    'histoire': 'histoire',
    'mer': ' mer',
    'fete': 'fete',
    'sport': 'sport',
    'ski': 'ski',
    'surf': 'surf',
    'culturel': 'culturel',
    'ile': 'ile',
    'desert': 'desert',
    'shopping': 'shopping',
    'aventure': 'aventure',
    'nature': 'nature',
    'attraction': 'attraction',
    'europe': 'europe',
    'asie': 'asie',
    'amerique': 'amerique',
    'afrique': 'afrique',
    'volcan': 'volcan',
    'neige': 'neige',
    'fr': 'france',
    'en': 'angleterre',
    'it': 'italie',
    'es': 'espagne',
    'au': 'australie',
    'ca': 'canada',
    'us': 'etatsunis',
    'ma': 'maroc',
    'th': 'thailande',
    'uae': 'emirats arabes unis',
    'ch': 'chine',
    'is': 'islande',
    'mgc': 'madagascar'
}

NEGATION = ['pas', 'sans']

CONJUNCTION = [' mais ', ' ou ', ' et ']

CITIES = [
    {
        'where': 'paris',
        'tags': [
            TAGS['urbain'],
            TAGS['visite'],
            TAGS['histoire'],
            TAGS['culturel'],
            TAGS['chic'],
            TAGS['archi'],
            TAGS['shopping'],
            TAGS['attraction'],
            TAGS['europe'],
            TAGS['fr']
        ]
    },
    {
        'where': 'marseille',
        'tags': [
            TAGS['urbain'],
            TAGS['chaud'],
            TAGS['mer'],
            TAGS['soleil'],
            TAGS['calme'],
            TAGS['culturel'],
            TAGS['prix moyen'],
            TAGS['bon marche'],
            TAGS['europe'],
            TAGS['fr']
        ]
    },
    {
        'where': 'chamonix',
        'tags': [
            TAGS['rural'],
            TAGS['froid'],
            TAGS['sport'],
            TAGS['montagne'],
            TAGS['ski'],
            TAGS['neige'],
            TAGS['prix moyen'],
            TAGS['chic'],
            TAGS['paysage'],
            TAGS['europe'],
            TAGS['nature'],
            TAGS['fr']
        ]
    },
    {
        'where': 'londres',
        'tags': [
            TAGS['urbain'],
            TAGS['fete'],
            TAGS['visite'],
            TAGS['culturel'],
            TAGS['chic'],
            TAGS['archi'],
            TAGS['shopping'],
            TAGS['europe'],
            TAGS['en']
        ]
    },
    {
        'where': 'rome',
        'tags': [
            TAGS['archi'],
            TAGS['visite'],
            TAGS['chaud'],
            TAGS['soleil'],
            TAGS['histoire'],
            TAGS['culturel'],
            TAGS['prix moyen'],
            TAGS['europe'],
            TAGS['it']
        ]
    },
    {
        'where': 'toscane',
        'tags': [
            TAGS['rural'],
            TAGS['paysage'],
            TAGS['calme'],
            TAGS['soleil'],
            TAGS['prix moyen'],
            TAGS['bon marche'],
            TAGS['europe'],
            TAGS['it']
        ]
    },
    {
        'where': 'barcelone',
        'tags': [
            TAGS['chaud'],
            TAGS['mer'],
            TAGS['fete'],
            TAGS['soleil'],
            TAGS['culturel'],
            TAGS['prix moyen'],
            TAGS['bon marche'],
            TAGS['shopping'],
            TAGS['attraction'],
            TAGS['europe'],
            TAGS['es']
        ]
    },
    {
        'where': 'minorque',
        'tags': [
            TAGS['chaud'],
            TAGS['rural'],
            TAGS['mer'],
            TAGS['calme'],
            TAGS['ile'],
            TAGS['prix moyen'],
            TAGS['chic'],
            TAGS['paysage'],
            TAGS['europe'],
            TAGS['es']
        ]
    },
    {
        'where': 'montreal',
        'tags': [
            TAGS['urbain'],
            TAGS['froid'],
            TAGS['fete'],
            TAGS['sport'],
            TAGS['neige'],
            TAGS['prix moyen'],
            TAGS['chic'],
            TAGS['amerique'],
            TAGS['ca']
        ]
    },
    {
        'where': 'sidney',
        'tags': [
            TAGS['sport'],
            TAGS['chaud'],
            TAGS['mer'],
            TAGS['soleil'],
            TAGS['surf'],
            TAGS['prix moyen'],
            TAGS['chic'],
            TAGS['shopping'],
            TAGS['au']
        ]
    },
    {
        'where': 'brisbane',
        'tags': [
            TAGS['soleil'],
            TAGS['chaud'],
            TAGS['chic'],
            TAGS['mer'],
            TAGS['sport'],
            TAGS['surf'],
            TAGS['paysage'],
            TAGS['au']
        ]
    },
    {
        'where': 'new york',
        'tags': [
            TAGS['urbain'],
            TAGS['visite'],
            TAGS['chic'],
            TAGS['shopping'],
            TAGS['amerique'],
            TAGS['us']
        ]
    },
    {
        'where': 'San Francisco',
        'tags': [
            TAGS['urbain'],
            TAGS['archi'],
            TAGS['chic'],
            TAGS['culturel'],
            TAGS['shopping'],
            TAGS['amerique'],
            TAGS['paysage'],
            TAGS['us']
        ]
    },
    {
        'where': 'marrakech',
        'tags': [
            TAGS['soleil'],
            TAGS['chaud'],
            TAGS['desert'],
            TAGS['culturel'],
            TAGS['afrique'],
            TAGS['paysage'],
            TAGS['bon marche'],
            TAGS['ma']
        ]
    },
    {
        'where': 'dubai',
        'tags': [
            TAGS['soleil'],
            TAGS['urbain'],
            TAGS['chaud'],
            TAGS['desert'],
            TAGS['chic'],
            TAGS['mer'],
            TAGS['shopping'],
            TAGS['attraction'],
            TAGS['afrique'],
            TAGS['uae']
        ]
    },
    {
        'where': 'hong kong',
        'tags': [
            TAGS['shopping'],
            TAGS['chic'],
            TAGS['culturel'],
            TAGS['asie'],
            TAGS['urbain'],
            TAGS['histoire'],
            TAGS['ch']
        ]
    },
    {
        'where': 'pekin',
        'tags': [
            TAGS['visite'],
            TAGS['prix moyen'],
            TAGS['culturel'],
            TAGS['asie'],
            TAGS['urbain'],
            TAGS['histoire'],
            TAGS['nature'],
            TAGS['paysage'],
            TAGS['ch']
        ]
    },
    {
        'where': 'bangkok',
        'tags': [
            TAGS['fete'],
            TAGS['bon marche'],
            TAGS['culturel'],
            TAGS['asie'],
            TAGS['nature'],
            TAGS['paysage'],
            TAGS['aventure'],
            TAGS['th']
        ]
    },
    {
        'where': 'hawaii',
        'tags': [
            TAGS['bon marche'],
            TAGS['culturel'],
            TAGS['amerique'],
            TAGS['rural'],
            TAGS['nature'],
            TAGS['ile'],
            TAGS['aventure'],
            TAGS['sport'],
            TAGS['surf'],
            TAGS['paysage'],
            TAGS['volcan'],
            TAGS['us']
        ]
    },
    {
        'where': 'everest',
        'tags': [
            TAGS['bon marche'],
            TAGS['culturel'],
            TAGS['asie'],
            TAGS['rural'],
            TAGS['nature'],
            TAGS['aventure'],
            TAGS['sport'],
            TAGS['paysage'],
            TAGS['montagne'],
            TAGS['neige'],
            TAGS['froid'],
            TAGS['ch']
        ]
    },
    {
        'where': 'reykjavik',
        'tags': [
            TAGS['prix moyen'],
            TAGS['europe'],
            TAGS['rural'],
            TAGS['nature'],
            TAGS['aventure'],
            TAGS['paysage'],
            TAGS['montagne'],
            TAGS['froid'],
            TAGS['volcan'],
            TAGS['is']
        ]
    },
    {
        'where': 'la reunion',
        'tags': [
            TAGS['prix moyen'],
            TAGS['afrique'],
            TAGS['rural'],
            TAGS['nature'],
            TAGS['paysage'],
            TAGS['montagne'],
            TAGS['chaud'],
            TAGS['volcan'],
            TAGS['soleil'],
            TAGS['mer'],
            TAGS['sport'],
            TAGS['surf'],
            TAGS['ile'],
            TAGS['fr']
        ]
    },
    {
        'where': 'antananarivo',
        'tags': [
            TAGS['ile'],
            TAGS['afrique'],
            TAGS['rural'],
            TAGS['nature'],
            TAGS['aventure'],
            TAGS['paysage'],
            TAGS['mer'],
            TAGS['soleil'],
            TAGS['bon marche'],
            TAGS['mgc']
        ]
    },
]
