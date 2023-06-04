import yaml

DATA_IN = {'items': ['computer', 'printer', 'keyboard', 'mouse'],
           'items_quantity': 4,
           'items_price': {'computer': '200€-1000€',
                           'printer': '100€-300€',
                           'keyboard': '5€-50€',
                           'mouse': '4€-7€'}
           }


def write_yaml(data, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        yaml.dump(data, file, default_flow_style=False, allow_unicode=True, sort_keys=False)


def read_yaml(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return yaml.load(file, Loader=yaml.SafeLoader)


if __name__ == '__main__':
    write_yaml(DATA_IN, 'data.yaml')

    if DATA_IN == read_yaml('data.yaml'):
        print("Данные совпадают")
    else:
        print("Данные не совпадают")
