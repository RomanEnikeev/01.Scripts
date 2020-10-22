tree = {
    'Stocks_75':
        {
            'World_10':
                'Fond_100',

            'Развивающие_40':
                {
                    'Russia_80':
                        'Stocks_100',
                    'Китай_20':
                        'Fond_100'
                },

            'Развитые_50':
                {'US_70': 'Fond_100',
                 'DE_30': 'Fond_100'
                 }

        },
    'Bonds_20': 'OFZ_100',
    'Gold_5': 'Fond_100'

}
# tree = {1: {2: 3, 4: 2}}

# print(tree['Stocks_75'])
print(type(tree['Stocks_75']))


def preorder(tree, capital, koef=1, koef_vetki=1):
    for key in tree.keys():
        if type(tree[key]) == dict:
            koef = koef * int(key.split('_')[1]) / 100
            preorder(tree[key], capital, koef=koef, koef_vetki=koef)
        else:
            koef = koef * int(key.split('_')[1]) / 100
            konechnaya = tree[key]
            tree[key] = tree.get(konechnaya, str(konechnaya) + '_' + str(koef) + '_' + str(koef*capital))
        koef = koef_vetki




capital = 76200
print(preorder(tree, capital))
print(tree)

