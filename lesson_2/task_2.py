import json


def write_order_to_json(item, quantity, price, buyer, date):

    with open('orders.json', 'r+', encoding='utf-8') as file:
        data = json.load(file)
        file.seek(0)
        file.truncate()
        orders_list = data['orders']
        order_info = {'item': item, 'quantity': quantity,
                      'price': price, 'buyer': buyer, 'date': date}
        orders_list.append(order_info)
        json.dump(data, file, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    write_order_to_json('футболка', '10', '300', 'Синсей', '05.06.2023')
    write_order_to_json('джинсы', '200', '1500', 'Зара', '23.06.2023')
    write_order_to_json('кроссовки', '100', '5000', 'Адидас', '07.06.2023')
    write_order_to_json('шорты', '50', '1000', 'Пума', '09.06.2023')
    write_order_to_json('носки', '1000', '100', 'Найк', '11.06.2023')
