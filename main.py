import pymongo

import time

from consts import LOCALHOST, DOCKER_PORT, LOCAL_PORT, MONGO_CONNECTION

try:

    conn = int(input("1 - local\n2 - with Docker\n3 - Cloud\n"))

    # Create the client
    if conn == 1:
        client = pymongo.MongoClient(LOCALHOST, LOCAL_PORT)
    elif conn == 2:
        client = pymongo.MongoClient(LOCALHOST, DOCKER_PORT)
    elif conn == 3:
        client = pymongo.MongoClient(MONGO_CONNECTION)
    else:
        print("Incorrect number")

    # Connect to our database
    db = client['mongo']

    # Fetch our series collection
    series_collection = db['mobile']
    mobile = db.mobile
    while True:

        num = int(input('0 - Exit \n1 - Insert \n2 - Find\n3 - Drop\n'))
        if not num:
            break
        elif num == 1:
            count_of_inserts = int(input("Count of inserts: 10/50/100/1000/...\n"))
            start = time.time()
            for i in range(count_of_inserts // 10):
                new_mobiles = [{"model": "Lenovo Legion Y90",
                                "price": 70000},
                               {"model": "Huawei P50 Pocket",
                                "price": 225000},
                               {"model": "Samsung Galaxy S22 Ultra",
                                "price": 125000},
                               {"model": "Samsung Galaxy S22+",
                                "price": 95000},
                               {"model": "Samsung Galaxy S22",
                                "price": 115000},
                               {"model": "Huawei Honor 60 SE 5G",
                                "price": 28500},
                               {"model": "Xiaomi 12X",
                                "price": 26000},
                               {"model": "Xiaomi 12 Pro",
                                "price": 55000},
                               {"model": "Motorola Edge X30",
                                "price": 55000},
                               {"model": "Xiaomi POCO M4 Pro",
                                "price": 45000}]
                mobile.insert_many(new_mobiles)
                end = time.time()
            print(f'Data have been successfully inserted\n Operation time: {round((end - start) * 1000)} ms')

        elif num == 2:
            num_1 = int(input('1 - Display all objects \n2 - Display by model\n3 - Display by price\n4 - Display '
                              'by model & price\n'))
            if num_1 == 1:
                start = time.time()
                for mobiles in mobile.find():
                    print(mobiles)
                end = time.time()
                print(f'Operation time: {round((end - start) * 1000)} ms')
            elif num_1 == 2:
                model = input("Input model: ")
                start = time.time()
                for mobiles in mobile.find({"model": model}):
                    print(mobiles)
                end = time.time()
                print(f'Operation time: {round((end - start) * 1000)} ms')
            elif num_1 == 3:
                price = int(input("input price: "))
                start = time.time()
                for mobiles in mobile.find({"price": price}):
                    print(mobiles)
                end = time.time()
                print(f'Operation time: {round((end - start) * 1000)} ms')
            elif num_1 == 4:
                model = input("Input model: ")
                price = int(input("input price: "))
                start = time.time()
                for mobiles in mobile.find({"model": model,
                                            "price": price}):
                    print(mobiles)
                end = time.time()
                print(f'Operation time: {round((end - start) * 1000)} ms')
            else:
                print('Incorrect number')
        elif num == 3:
            mobile.drop()
        else:
            print('Incorrect number')

except Exception as error:
    print('Error while working with mongoDB', error)

finally:
    print('Connection with mongoDB closed')
