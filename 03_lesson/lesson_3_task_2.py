from smartphone import Smartphone


catalog = []


def add_to_catalog(*phone: str):
    catalog.append(Smartphone(*phone))


phone1 = Smartphone("Apple", "Pro 15", "9234567891")
phone2 = Smartphone("Xiaomi", "Mi15S", "9876543212")
phone3 = Smartphone("Nokia", "3310", "9631254878")
phone4 = Smartphone("Siemens", "L1234", "9516327841")
phone5 = Smartphone("Sony", "W310", "9321598765")


[catalog.append(eval(f"phone{i}")) for i in range(1, 6)]
[print(phone) for phone in catalog]
