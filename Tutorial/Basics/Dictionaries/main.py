
monthConversion = {
    "Jan" : "January",
    "Feb" : "Febraury",
    "Mar" : "March",
    "Apr" : "April",
    67 : "May",
    5: "June",
   }

print(monthConversion["Feb"])
print(monthConversion.get("Feb"))
print(monthConversion.get("qfw"))
print(monthConversion.get("qfw", "Gibts nicht"))
any = input("Month: ")
print(monthConversion[any])