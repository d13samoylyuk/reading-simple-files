from pprint import pprint


def get_shop_list_by_dishes(dishes, person_count):
    ingres = {}
    all_dishes = convert_recipes(read_file('recipier/recipes.txt'))
    for dish in all_dishes:
        if dish not in dishes:
            continue
        ingredients = all_dishes[dish]
        for ingredient in ingredients:
            if ingredient['ingredient_name'] not in ingres:
                ingres[ingredient['ingredient_name']] = {
                    'measure': ingredient['measure'],
                    'quantity': 0
                }
            ingres[ingredient['ingredient_name']]['quantity'] += (
                ingredient['quantity'] * person_count)

    return ingres


def read_file(filename, encoding='UTF-8', as_lines=True):
    with open(filename, encoding=encoding) as file:
        if as_lines:
            return [line.strip() for line in file.readlines()]
        return file.read()


def convert_recipes(file):
    cook_book = {}
    current_dish = None
    for line in file:
        if line.isdigit() or line == '':
            continue
        line = line.split(' | ')
        if len(line) == 1:
            cook_book[line[0]] = []
            current_dish = line[0]
        else:
            template = {
                'ingredient_name': line[0],
                'quantity': int(line[1]),
                'measure': line[2]
            }
            cook_book[current_dish].append(template)

    return cook_book


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
print()
pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 1))