import json

data = [

    {
        "name":"aryan",
        "roll":"1"
     },

     {
         "name":"shiva",
         "roll":"2"
     }
]

##read
data_js = json.loads(data)
##print the json data
for api in data_js:
    print(api)


##dumpsfor saving
data_a = json.dumps(data)
file = open("output.json","w")
file.write(data_a)
file.close()
