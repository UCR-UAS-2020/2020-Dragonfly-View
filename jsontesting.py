import json


with open('auvsi-example.json') as f:
    datDict = json.load(f)
    print(datDict)

obj_type = datDict['type']

try:
    nullKey = datDict['noSuchListing']
except KeyError:
    print('No Key Matching noSuchListing')
except ZeroDivisionError:
    print('DivideByZero')
finally:
    nullType = None

