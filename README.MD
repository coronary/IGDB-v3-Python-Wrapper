#Python Wrapper for IGDB Api
More detailed readme coming later.

##instantiate igdb object from json file with your api key indexed by api-key

with open('key.json') as keyFile:
    key = json.load(keyFile)
    key = key['api-key']
igdbObj = igdb(key)

##Create list of strings used in your query

requestData = [igdbObj.fields('name','platforms.name','genres.name'), igdbObj.where(igdbObj.orry(igdbObj.equals('platforms','48'), igdbObj.notEq('platforms','49'))), igdbObj.limit(2)]

##Make your request using the buildRequest function 
r = igdbObj.buildRequest('games', re).json()

##Profit

