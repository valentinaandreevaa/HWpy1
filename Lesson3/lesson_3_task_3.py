from address import Address
from mailing import Mailing

to_address = Address("664022", "Irkutsk", "Lenina", "22", "1")
from_address = Address("111111", "ivanovo", "Lenina", "11", "2")
mailing = Mailing(to_address, from_address, "555", "Tdd123")

print(f"отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
       f"{mailing.from_address.street}, {mailing.from_address.house}, {mailing.from_address.apartment}"
      f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street},"
      f"{mailing.to_address.house}, {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей." )