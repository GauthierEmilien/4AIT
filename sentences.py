""" ALL WHITESPACE BEFORE WORDS ARE VERY IMPORTANT, DO NOT DELETE THEM"""

SENTENCES = {
    'bonjour': 'Bonjour, que puis-je faire pour vous ?',
    'not_understand': 'Désolé, je ne comprends pas',
    'react_to_proposition': [
        'Dites m\'en plus sur vos attentes',
        'Je vois, quelque chose d\'autre ?',
        'C\'est noté. Quoi d\'autres ?'
    ]
}

DESCRIPTION_WORDS = ['dites', 'savoir', 'plus', 'dire', 'info', 'informations']

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
        ],
        'description': 'Paris est la capitale de la France, grande ville européenne et un centre mondial de l\'art, '
                       'de la mode, de la gastronomie et de la culture. Outre les monuments comme la tour Eiffel et '
                       'la cathédrale gothique Notre-Dame du XIIe siècle, la ville est réputée pour ses cafés et ses '
                       'boutiques de luxe bordant la rue du Faubourg-Saint-Honoré.',
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
        ],
        'description': 'Marseille, ville portuaire du sud de la France, fondée par les Grecs vers 600 av. J.-C. En '
                       'son cœur se trouve le Vieux-Port. La basilique Notre-Dame-de-la-Garde est une église romane '
                       'd\'inspiration byzantine. '
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
        ],
        'description': 'Station de villégiature à la jonction de la France, de la Suisse et de l\'Italie. Située au '
                       'pied du Mont-Blanc, le plus haut sommet des Alpes, elle est réputée pour ses pistes de ski. '
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
        ],
        'description': 'Londres, la capitale de l\'Angleterre et du Royaume-Uni, est une ville moderne dont '
                       'l\'histoire remonte à l\'époque romaine. En son centre se dressent le Parlement, Big Ben et '
                       'l\'abbaye de Westminster, lieu de couronnement des monarques britanniques. '
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
        ],
        'description': 'Capitale de l\'Italie, Rome est une grande ville cosmopolite dont l\'art, l\'architecture et '
                       'la culture de presque 3 000 ans rayonnent dans le monde entier. Ses ruines telles que celles '
                       'du Forum Romain et du Colisée évoquent la puissance de l\'ancien Empire romain. '
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
        ],
        'description': 'La Toscane est une région du centre de l\'Italie. Sa capitale, Florence, abrite une partie de '
                       'l\'art et de l\'architecture de la Renaissance la plus reconnaissable au monde, notamment le '
                       'David de Michel-Ange, les œuvres de Botticelli exposées dans la galerie des Offices et la '
                       'cathédrale Santa Maria del Fiore '
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
        ],
        'description': 'Barcelone, la capitale cosmopolite de la région espagnole de Catalogne, est réputée pour son '
                       'art et son architecture. La basilique de la Sagrada Família et d\'autres bâtiments '
                       'emblématiques conçus par Antoni Gaudí sont de parfaits exemples du modernisme catalan '
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
        ],
        'description': 'Minorque est l\'une des îles espagnoles des Baléares situées dans la mer Méditerranée. '
                       'Traditionnellement plus calme que Majorque et Ibiza, qui se trouvent à proximité, '
                       'elle est réputée pour ses plages à perte de vue. '
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
        ],
        'description': 'Montréal est la deuxième ville la plus peuplée du Canada. Elle se situe principalement sur '
                       'l’île fluviale de Montréal, sur le fleuve Saint-Laurent dans le Sud du Québec, dont elle est '
                       'la métropole. '
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
        ],
        'description': 'Sydney, capitale de la Nouvelle-Galles du Sud et l\'une des plus grandes villes d\'Australie, '
                       'est renommée pour son opéra situé dans le port, avec son design distinctif en forme de voiles. '
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
        ],
        'description': 'Brisbane, capitale de l\'État du Queensland, est une grande ville qui s\'étend sur le fleuve '
                       'Brisbane. Son centre culturel, le quartier de South Bank ("rive sud"), abrite le musée du '
                       'Queensland et le Sciencentre, qui propose des expositions interactives. '
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
        ],
        'description': 'New York est une ville des Etats Unis. En son centre se trouve Manhattan, faisant partie des '
                       'principaux centres commerciaux, financiers et culturels du monde. Ses sites incontournables '
                       'comprennent des gratte-ciel comme l\'Empire State Building et l\'immense Central Park. Le '
                       'théâtre de Broadway est situé sur Times Square. '
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
        ],
        'description': 'San Francisco, en Californie du Nord, est une ville vallonnée à la pointe d\'une péninsule '
                       'entourée par l\'océan Pacifique et la baie de San Francisco. Elle est célèbre pour son '
                       'brouillard permanent, l\'emblématique pont du Golden Gate, ses Cable Cars et ses maisons '
                       'victoriennes colorées '
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
        ],
        'description': 'Marrakech, ancienne cité impériale de l\'ouest du Maroc, et un centre économique majeur '
                       'abritant des mosquées, des palais et des jardins. La médina est une cité médiévale fortifiée '
                       'datant de l\'Empire berbère, avec des allées entremêlées tel un labyrinthe, où les souks ('
                       'marchés) animés vendent des étoffes, des poteries et des bijoux traditionnels. Symbole de la '
                       'ville, le minaret de la mosquée maure de Koutoubia du XIIe siècle est visible à des '
                       'kilomètres. '
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
        ],
        'description': 'Dubaï est une ville et un émirat des Émirats arabes unis réputé pour son shopping de luxe, '
                       'son architecture ultramoderne et sa vie nocturne animée. La Burj Khalifa, tour de 830 mètres '
                       'de haut, domine le paysage urbain parsemé de gratte-ciel. À son pied, la fontaine de Dubaï '
                       'présente des jets et des lumières synchronisés avec de la musique. '
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
        ],
        'description': 'Ancienne colonie britannique, Hong Kong est un territoire indépendant situé au sud-est de la '
                       'Chine. Central (le quartier d\'affaires) comporte de nombreux monuments architecturaux comme '
                       'la tour de la Bank of China, conçue par I.M. Pei. Hong Kong est aussi très prisé pour le '
                       'shopping, avec ses célèbres tailleurs sur mesure et le marché nocturne de Temple Street. '
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
        ],
        'description': 'Beijing (ou Pékin), l’immense capitale chinoise, est empreinte d’une histoire de plus de 3 '
                       'millénaires. Elle est connue aussi bien pour son architecture moderne que pour ses sites '
                       'anciens tels que le grand palais impérial de la Cité interdite, dont la construction date des '
                       'dynasties Ming et Qing. L’immense place piétonne Tian Anmen, abrite le mausolée de Mao Zedong '
                       'et le musée national de Chine. '
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
        ],
        'description': 'Bangkok, la capitale de la Thaïlande, est une grande ville connue pour ses sanctuaires '
                       'richement décorés et ses rues animées. Rempli de bateaux, L\'opulent Grand Palais et son '
                       'temple sacré Wat Phra Kaeo. À proximité, le temple Wat Pho dispose d\'un énorme Bouddha '
                       'allongé et, sur la rive opposée, le temple Wat Arun est doté d\'escaliers raides et d\'une '
                       'flèche de style Khmer. '
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
        ],
        'description': 'Hawaii, un État américain, est un archipel volcanique isolé dans le Pacifique central. Ses '
                       'îles sont réputées pour leurs paysages accidentés composés de falaises, de chutes d\'eau, '
                       'de forêt tropicale et de plages dont le sable arbore des teintes dorées, rouges, noires, '
                       'voire vertes. '
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
        ],
        'description': 'L\'Evrest, aussi appelé mont Everest, est une montagne située dans la chaîne de l\'Himalaya, '
                       'à la frontière entre le Népal et la Chine. Est le plus haut sommet du monde. '
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
        ],
        'description': 'Sur la côte islandaise, Reykjavik est la capitale et la plus grande ville du pays. Elle '
                       'inclut le musée national et le musée des Sagas qui retracent l\'histoire des Vikings '
                       'd\'Islande. La Hallgrímskirkja, une impressionnante église en béton, et le Perlan, '
                       'avec son dôme en verre rotatif, offrent une vue dégagée sur la mer et les collines voisines. '
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
        ],
        'description': 'L\'île de la Réunion est un département français de l\'océan Indien. Elle est réputée pour '
                       'son intérieur volcanique recouvert de forêt tropicale, ses récifs de corail et ses plages. '
                       'Son site le plus emblématique est le piton de la Fournaise, un volcan actif qui peut être '
                       'gravi et s\'élève à 2 632 m d\'altitude. '
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
        ],
        'description': 'Antananarivo est la capitale de Madagascar, située dans la région des Hautes Terres centrales '
                       'de l\'île. Surplombant la ville, le palais Rova de Manjakamiadana fut le cœur du royaume des '
                       'Merina à partir du XVIIe siècle. Il abrite des maisons en bois et des tombeaux royaux. Le '
                       'palais baroque rose d\'Andafiavaratra se trouve dans le quartier proche de la Haute Ville. '
    },
]
