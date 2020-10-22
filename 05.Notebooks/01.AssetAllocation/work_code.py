# тут выбираем агрессивное распределение активов на долгосрок: 75 процентов акции (Stocks),
# 20 - облигации и 5 процентов на золото

# далее акции делим на инвестиции в акции всего мира 10 процентов (тикер FXWO), акции в развивающие страны 40
# процентов и 50 процентов на развитые страны. Акции всего мира это фонд от Finex (FXWO и FXRW), в данном случае 100
# процентов идут в фонд (или 0.75*0.1*1 = 0.225 от всего капитала - число, которое мы получим на выходе)

tree = {
    'Stocks_75':
        {
            'World_10':
                'Фонд_100',

            'Развивающие_40':
                {
                    'Russia_80':
                        'Акции_100',
                    'Китай_20':
                        'Фонд_100'
                },

            'Развитые_50':
                {'США_70': 'Fond_100',
                 'Германия_30': 'Fond_100'
                 }

        },
    'Облигации_20': 'OFZ_100',
    'Золото_5': 'Fond_100'

}


def preorder(tree, capital, koef=1, koef_vetki=1):
    for key in tree.keys():
        if type(tree[key]) == dict:
            koef = koef * int(key.split('_')[1]) / 100
            preorder(tree[key], capital, koef=koef, koef_vetki=koef)
        else:
            koef = koef * int(key.split('_')[1]) / 100
            konechnaya = tree[key]
            tree[key] = tree.get(konechnaya, str(konechnaya) + '_' + str(koef) + '_' + str(koef * capital))
        koef = koef_vetki


capital = 10000  # инвестируемая сумма

preorder(tree, capital)   # выполняем распределение активов
print(tree)
