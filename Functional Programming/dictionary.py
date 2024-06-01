myDict = {
    "regigigas": "slow start",
    "shedinja": "wonder guard",
    "entries": [1, 2],
    "myDict2": {
        "hp1": 120,
        "hp2": 1
    },
    1024: 1
}
# myDict["entries"]=[2]
# print(myDict["regigigas"])
# print(myDict["shedinja"])
# print(myDict["entries"])
# print(myDict["myDict2"]["hp1"])

# dictionary methods
# print(list(myDict.keys())) # print the keys as list
# print(myDict.values()) # print the values
# print(myDict.items()) # print keys & values as list
print(myDict)
udDict = {
    "mega zard X": "tough claws",
    "mega zard Y": "drought"
}
myDict.update(udDict)  # update the myDict by adding key-value pairs
print(myDict)
print(myDict.get("shedinja"))
# 'get' returns none value if element not present
print(myDict.get("shediinja"))
print(myDict["shedinja"])  # [] returns error if element not present
