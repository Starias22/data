import json as js
#deserilization from file;load
with open('Sample.json','r') as strm:
    data=js.load(fp=strm)
    print(data)
    print('type(data):',type(data))

#deserilization from string:loads
json_var ="""
{
	"Country": {
		"name": "INDIA",
		"Languages_spoken": [
			{
				"names": ["Hindi", "English", "Bengali", "Telugu"]
			}
		]
	}
}
"""
var = js.loads(json_var)
print(var)
print(type(var))
