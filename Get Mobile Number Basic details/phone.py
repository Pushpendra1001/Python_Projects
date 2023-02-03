import phonenumbers
from phonenumbers import timezone,geocoder,carrier,phonemetadata
number = input("Enter Your NO with +91: ")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone,"en")
reg=geocoder.description_for_number(phone,"en")

print(phone)
print(time)
print(car)
print(reg)

input("Enter For exit")
