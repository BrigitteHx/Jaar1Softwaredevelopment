# fruitmandopdracht10

from fruitmand import fruitmand
from operator import itemgetter

fruitmand = sorted(fruitmand , key = itemgetter('weight', 'name'), reverse=True)
# sorted sorteert de fruitmand op gewicht van licht naar zwaar (itemgetter weight), reverse draait deze om zodat de zwaarste bovenaan staat

for fruit in fruitmand: 
    print(fruit['weight'], fruit['name'])
# print voor de gehele fruit lijst het gewicht 
