import json


def reset_orders():
    with open('orders.json', 'w', encoding='utf-8') as file:
        json.dump({'orders': []}, file, indent=4)


if __name__ == "__main__":
    reset_orders()