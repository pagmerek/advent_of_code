from collections import defaultdict, Counter


def parse(raw):
    data = raw.split('\n')
    foods = set()
    all_ingred = Counter()
    all_allerg = defaultdict(list)
    for line in data:
        ingred, allerg = line.split(' (contains ')
        ingred = set(ingred.split(' '))
        allerg = set(allerg[:-1].split(', '))
        for x in allerg:
            all_allerg[x].append(ingred)
        all_ingred.update(ingred)
        foods.update(ingred)
    return foods, all_ingred, all_allerg


if __name__ == '__main__':
    with open('input') as f:
        data = f.read()
    foods, ings, allergens = parse(data)
    allerg2 = defaultdict(list)
    allerg3 = set()
    for i in allergens:
        for j in foods:
            if all(j in k for k in allergens[i]):
                allerg2[i].append(j)
                allerg3.add(j)
    print(sum(ings[x] for x in (foods - allerg3)))

    allerg4 = []
    while allerg2:
        found = None
        for x in allerg2:
            if len(allerg2[x]) == 1:
                found = x
                break
        if not found:
            break
        allg = allerg2[found][0]
        allerg4.append((found, allg))
        del allerg2[found]
        for x in allerg2:
            try:
                allerg2[x].remove(allg)
            except ValueError:
                pass
            
    allerg4.sort()
    print(','.join(x[1] for x in allerg4))
