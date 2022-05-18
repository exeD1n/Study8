def decorator(x):
    def calc_cube(r):
        print('Start decorator')
        x(r)
        print('Finish decorator')

    return calc_cube


def say(chislo):
    names_dict_list = dict()
    names_dict_list.update({chislo ** 5: type(chislo ** 5)})
    print(names_dict_list)

    with open("log.txt", "w") as file:
        file.write(str(names_dict_list))


say = decorator(say)
say(5.0)
