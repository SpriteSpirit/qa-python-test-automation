from address import Address
from mailing import Mailing


to_address = Address(123456, "Нью Йорк", "Аврора авеню", 25, 36)
from_address = Address(987654, "Саратов", "ул. Ленина", 74, 95)

mailing = Mailing(to_address, from_address, 1234.56, "US-RU-NS0009513574682")
print(mailing)
