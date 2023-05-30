from glob import glob
import re


def get_data():

    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = ["Изготовитель системы", "Название ОС", "Код продукта", "Тип системы"]

    for info in glob("info_*.txt"):
        with open(info, encoding="cp1251") as file:
            data = file.read()
            os_prod_list.append(re.findall(r"Изготовитель системы:\s*\S*", data)[0].split()[2])
            os_name_list.append(re.findall(r"Windows\s\S*", data)[0])
            os_code_list.append(re.findall(r"Код продукта:\s*\S*", data)[0].split()[2])
            os_type_list.append(re.findall(r"Тип системы:\s*\S*", data)[0].split()[2])

    return [main_data, *zip(os_prod_list, os_name_list, os_code_list, os_type_list)]


def write_to_csv(out_file):
    """Запись данных в csv"""

    main_data = get_data()
    with open(out_file, "w", encoding="utf-8") as file:
        for row in main_data:
            file.write(f"{','.join(row)}\n")


if __name__ == "__main__":
    write_to_csv('task_1.csv')
