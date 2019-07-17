import requests

class igdb:
    def __init__(self, key):
        self.key = {'user-key': key}
        self.baseUrl = 'https://api-v3.igdb.com'
        self.lastRequest = None
        
    def __slashName(self, name) -> str:
        #Name needs to be double quoted to work
        return "\"" + name + "\""

    def __command(self, command: str, data: tuple) -> str:
        #builds command by concatenating the desired command with the data and then a semi colon. tuple must be of strings
        return command + ' ' + ', '.join(data) + ";"

    def __filterTrans(self, firstArg, secondArg, operator) -> str:
        #Utility function for the filter options in the api
        if (firstArg == 'name'):
            secondArg = self.__slashName(secondArg)
        return firstArg + ' ' + operator + ' ' + secondArg 
    
    def limit(self, num: int) -> str:
        # returns 'limit = num;'
        return self.__command('limit', (str(num),))
    
    # FILTERS

    def andy(self, firstArg, secondArg) -> str:
        # used for the and filter. sample output 'firstArg = secondArg'
        return self.__filterTrans(firstArg, secondArg, '&')

    def equals(self, field: str, desired: str) -> str:
        # used for the equals filter. sample output 'field = desired'
        return self.__filterTrans(field, desired, '=')

    def less(self, field: str, number: int) -> str:
        # used for the less than filter. sample output 'field < number'
        return self.__filterTrans(field, number, '<')
        
    def greater(self, field: str, number: int) -> str:
        # used for the greater than filter. sample output 'field > number'
        return self.__filterTrans(field, number, '>')

    def greatEq(self, field: str, number: int) -> str:
        # used for the greater than or equal filter. sample output 'field >= number'
        return self.__filterTrans(field, number, '>=')

    def lessEq(self, field: str, number: int) -> str:
        # used for the less than or equal filter. sample output 'field <= number'
        return self.__filterTrans(field, number, '<=')

    #idk what to categorize this as
    def fields(self, *data: str) -> str:
        # defines the fields you want to be returned in your query. Takes in as many strings as you like
        return self.__command('fields', data)
    
    def where(self, *data) -> str:
        # generates where command
        data = self.__command('where', data)
        return data

    #REQUEST METHODS
    def buildRequest(self, requestType: str, requestStrings: list):
        return self.__sendRequest(requestType, ' '.join(requestStrings)) 
    
    def advancedRequest(self, requestType, requestString):
        return self.__sendRequest(requestType, requestString)

    def __sendRequest(self, requestType, data):
        url = self.baseUrl + '/' + requestType
        self.lastRequest = requests.post(url, headers=self.key, data=data)
        return self.lastRequest
        
        