s = (b"""b'POST /20220713202300.json HTTP/1.1\r\nHost: 192.168.0.78\r\nAccept: */*\r\nContent-Length: 817\r\nContent-Type: application/x-www-form-urlencoded\r\n\r\n{\n   "Body" : {\n      "Inverters" : {\n         "1" : {\n            "DT" : 126,\n            "E_Day" : 30282,\n            "E_Total" : 2564.4306640625,\n            "E_Year" : 3109156,\n            "P" : 32\n         }\n      },\n      "Site" : {\n         "E_Day" : 30282,\n         "E_Total" : 2564.4305555555557,\n         "E_Year" : 3109156,\n         "Meter_Location" : "unknown",\n         "Mode" : "produce-only",\n         "P_Akku" : null,\n         "P_Grid" : null,\n         "P_Load" : null,\n         "P_PV" : 32,\n         "rel_Autonomy" : null,\n         "rel_SelfConsumption" : null\n      },\n      "Version" : "12"\n   },\n   "Head" : {\n      "RequestArguments" : {}'""")
"""
import ast
import json

byte_str = s

#dict_str = byte_str.decode("UTF-8")
res = s.decode()
#res = res.replace("\n", "")

res = res.replace("            ", "")
res = res
print(res)
u = res.split("{", 1)[1]
#print(u)
#x = json.load(u)
#print(x)
#print(type(x))
#mydata = ast.literal_eval(dict_str)
#print(repr(mydata))
"""
import json

d = """{
   "Body" : {
      "Inverters" : {
         "1" : {
            "DT" : 126,
            "E_Day" : 30285,
            "E_Total" : 2564.4306640625,
            "E_Year" : 3109158.75,
            "P" : 0
         }
      },
      "Site" : {
         "E_Day" : 30285,
         "E_Total" : 2564.4305555555557,
         "E_Year" : 3109158.75,
         "Meter_Location" : "unknown",
         "Mode" : "produce-only",
         "P_Akku" : null,
         "P_Grid" : null,
         "P_Load" : null,
         "P_PV" : null,
         "rel_Autonomy" : null,
         "rel_SelfConsumption" : null
      },
      "Version" : "12"
   }
}"""

d = """""{
   "Body" : {
      "Inverters" : {
         "1" : {
            "DT" : 126,
            "E_Day" : 30285,
            "E_Total" : 2564.4306640625,
            "E_Year" : 3109158.75,
            "P" : 0
         }
      },
      "Site" : {
         "E_Day" : 30285,
         "E_Total" : 2564.4305555555557,
         "E_Year" : 3109158.75,
         "Meter_Location" : "unknown",
         "Mode" : "produce-only",
         "P_Akku" : null,
         "P_Grid" : null,
         "P_Load" : null,
         "P_PV" : null,
         "rel_Autonomy" : null,
         "rel_SelfConsumption" : null
      },
      "Version" : "12"
   }"""""


d = json.loads(d)

print(d)