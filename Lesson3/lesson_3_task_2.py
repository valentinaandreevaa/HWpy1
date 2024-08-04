from smartphone import Smartphone

catalog = []

phone1 = Smartphone("Iphone", "14 Pro", "+799999999")
phone2 = Smartphone("Samsung", "s21", "+7905553535")
phone3 = Smartphone("Xiaomi", "Mi9T", "+794444444")
phone4 = Smartphone("Nokia", "3310", "+76665532")
phone5 = Smartphone("Vivo", "11pro", "+798564123")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
