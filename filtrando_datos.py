DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    all_python_devs = [worker["name"]
                       for worker in DATA if worker["language"] == "python"]
    all_python_devs1 = list(filter(lambda worker: worker["language"] == "python", DATA))
    all_python_devs1 = list(map(lambda worker: worker["name"], all_python_devs1))
    
    all_platzi_workers = [tra["name"]
                          for tra in DATA if tra["organization"] == "Platzi"]
    all_platzi_workers1 = list(filter(lambda worker: worker["organization"] == "Platzi", DATA))
    all_platzi_workers1 = list(map(lambda worker: worker["name"], all_platzi_workers1))
    adults = list(filter(lambda item: item["age"] > 18, DATA))
    adults = list(map(lambda item: item["name"], adults))
    old_people = list(map(lambda worker: worker | {
                      "old": worker["age"] > 70}, DATA))

    # print("_______________________________________________")
    # print(all_python_devs)

    # for i in all_python_devs:
    #   print(i)

    # print("_______________________________________________")
    # print(all_python_devs1)

    # for i in all_python_devs1:
    #   print(i)

    print("_______________________________________________")
    print(all_platzi_workers)

    for i in all_platzi_workers:
      print(i)
    
    print("_______________________________________________")
    print(all_platzi_workers1)

    for i in all_platzi_workers1:
      print(i)

    # print("_______________________________________________")
    # print(adults)

    # for i in adults:
    #     print(i)

    # print("_______________________________________________")
    # # print(old_people)

    # for i in old_people:
    #     print(i)


if __name__ == '__main__':
    run()
