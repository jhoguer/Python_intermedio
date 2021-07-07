def run():
  my_list = [1, "hello", True, 4.5]
  my_dict = {"firstname": "Jhon Leider", "lastname": "Guerrero"}

  super_list = [
    {"firstname": "Jhon Leider", "lastname": "Guerrero"},
    {"firstname": "Simon", "lastname": "Vasquez"},
    {"firstname": "Pepe", "lastname": "Lopez"},
    {"firstname": "Galia", "lastname": "Guerrero"},
    {"firstname": "Thor Alejandro", "lastname": "Gato"},
  ]

  super_dict = {
    "natural_nums": [1, 2, 3, 4, 5],
    "integer_nums": [-1, -5, 0, 1, 3],
    "floating_nums": [1.1, 4.5, 6.43],
  }

  for key, value in super_dict.items():
     print(key, "-", value)

  for i in super_list:
    # print(i)
    print(i["firstname"], "-", i["lastname"])


if __name__ == '__main__':
  run()