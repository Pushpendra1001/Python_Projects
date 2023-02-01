import pywhatkit as kt

Your_NO = input("Enter Your Mobile Number add with country code like +91 : ")
message = input("Enter Your message 😉 :")
hr = int(input("Enter time in hr : "))
min = int(input("Enter Miniutes : "))

kt.sendwhatmsg(Your_NO,message , hr,min)