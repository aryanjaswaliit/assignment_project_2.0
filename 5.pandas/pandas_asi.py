import pandas as pd

json_d = [
    {
        "name":"Aryan",
        "roll":"1",
        "class":"12"
    },
    {
        "name":"Shiva",
        "roll":"2"
    }
]
old = pd.read_csv("output.csv")
print(old)


data =pd.DataFrame(json_d)

print(data)

new_data = pd.concat([data,old])
print(new_data)
new_data.to_csv("output.csv",index=False)