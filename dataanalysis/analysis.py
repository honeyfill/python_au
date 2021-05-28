import datetime
import matplotlib.pyplot as plt
from datetime import datetime as dt

year = 2020


def generate_date_resource(data, num):
    x_data, y_data = [], []
    d = filter_data(data, 'resource', '{}'.format(num), 'exact')
    for i in range(len(d)):
        x_data.append(d[i]['date'])
        y_data.append(int(d[i]['count']))
    return x_data, y_data


def generate_date_staff_id(data, num):
    x_data, y_data = [], []
    d = filter_data(data, 'staff_id', '{}'.format(num), 'exact')
    for i in range(len(d)):
        x_data.append(d[i]['date'])
        y_data.append(int(d[i]['count']))
    return x_data, y_data


def drawing_one_resource(data, num):
    x, y = generate_date_resource(data, num)
    plt.plot(x, y, color='black', marker="o")
    plt.title("Resource {}".format(num))
    plt.xlabel("date")
    plt.ylabel("count")
    plt.show()


def drawing_all_resource(data):
    for i in range(1, 11):
        x, y = generate_date_resource(data)
        plt.plot(x, y, color='black', marker="o")
        plt.title("Resource {}".format(i))
        plt.xlabel("date")
        plt.ylabel("count")
        plt.show()


def drawing_one_staff_id(data, num):
    x, y = generate_date_staff_id(data, num)
    plt.plot(x, y, color='black', marker="o")
    plt.title("staff_id {}".format(num))
    plt.xlabel("date")
    plt.ylabel("count")
    plt.show()


def drawing_all_staff_id(data):
    for i in range(1, 10):
        x, y = generate_date_staff_id(data, i)
        plt.plot(x, y, color='black', marker="o")
        plt.title("staff_id {}".format(i))
        plt.xlabel("date")
        plt.ylabel("count")
        plt.show()


def open_file(input_file):
    with open(input_file) as file:
        return list(map(lambda x: x.strip().split(','), file.readlines()))


def list_dict(input_file):
    data = open_file(input_file)
    head = data[0]
    return list(map(lambda x: dict(zip(head, x)), data[1::]))


def sort_key(data, key):
    if key in ['resource', 'count', 'staff_id']:
        return sorted(data, key=lambda x: int(x[key] if x[key] != '' else 0))
    if key == 'date':
        return sorted(data,
                      key=lambda x: dt.strptime(x[key], "%Y-%m") if x[key] != '' else datetime.datetime(1, 1, 1, 1, 1, 1, 1))


def filtration(data, x, value, arg):
    if data == 'date':
        arg_option = {'more': dt.strptime(x[data], "%Y-%m") > dt.strptime(value, "%Y-%m") if x[data] != '' else None,
                      'less': dt.strptime(x[data], "%Y-%m") < dt.strptime(value, "%Y-%m") if x[data] != '' else None,
                      'exact': dt.strptime(x[data], "%Y-%m") == dt.strptime(value, "%Y-%m") if x[data] != '' else None}
        return arg_option[arg]
    if data in ['resource', 'count', 'staff_id']:
        arg_option = {'more': int(x[data]) > int(value) if x[data] != '' else None,
                      'less': int(x[data]) < int(value) if x[data] != '' else None,
                      'exact': int(x[data]) == int(value) if x[data] != '' else None}
        return arg_option[arg]


def filter_data(data, key, value, arg):
    return list(filter(lambda x: filtration(key, x, value, arg), data))


def main():
    data_wo = sort_key(list_dict('data_without_id.csv'), 'date')
    data_w = sort_key(list_dict('data_with_id.csv'), 'date')
    drawing_one_resource(data_wo, 3)
    drawing_one_staff_id(data_w, 5)


if __name__ == '__main__':
    main()
