import requests

class igdb:
    def __init__(self, key):
        self.key = {'user-key': key}
        self.baseUrl = 'https://api-v3.igdb.com'
        self.lastRequest = None
        
    def __slashName(self, name) -> str:
        #Name needs to be double quoted to work
        # postfix etc made this function ugly
        first = "\""
        second = "\""
        if(name.endswith('*')):
            name = name[:-1]
            second = "\"*"
        if(name.startswith('*')):
            name = name[1:]
            first = "*\""
        if(name.startswith('*') and name.endswith('*')):
            name = name[1:-1]
            first = "*\""
            second = "\"*"
        return first + name + second

    def __command(self, command: str, data) -> str:
        #builds command by concatenating the desired command with the data and then a semi colon. tuple must be of strings
        if (type(data) == tuple):
            return command + ' ' + ', '.join(data) + ";"
        return command + ' ' + data + ';'

    def __filterTrans(self, firstArg, secondArg, operator) -> str:
        #Utility function for the filter options in the api
        if (firstArg == 'name'):
            secondArg = self.__slashName(secondArg)
        return firstArg + ' ' + operator + ' ' + secondArg 

    def __postpre(self, firstArg: str, secondArg: str) -> str:
        # returns the two input strings concatenated. Used for the postfix, prefix, infix functions
        return firstArg + secondArg

    def postfix(self, data: str):
        # returns input string with * in front of it 
        return self.__postpre('*', data)

    def prefix(self, data: str):
        # returns input string with * in after it 
        return self.__postpre(data, '*')

    def infix(self, data: str):
        # returns input string with * in front of it and behind it
        interim = self.__postpre(data, '*')
        return self.__postpre('*', interim)
    
    def limit(self, num: int) -> str:
        # returns 'limit = num;'
        return self.__command('limit', str(num))


    # FILTERS

    def orry(self, firstArg, secondArg) -> str:
        # used for the and filter. sample output 'firstArg = secondArg'
        return self.__filterTrans(firstArg, secondArg, '|')

    def andy(self, firstArg, secondArg) -> str:
        # used for the and filter. sample output 'firstArg = secondArg'
        return self.__filterTrans(firstArg, secondArg, '&')

    def equals(self, field: str, desired: str) -> str:
        # used for the equals filter. sample output 'field = desired'
        return self.__filterTrans(field, desired, '=')

    def insens(self, field: str, desired: str) -> str:
        # used for the insensitive filter. sample output 'field ~ desired'
        return self.__filterTrans(field, desired, '~')

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
        
        
#   NEW STUFF
    def square(self, inputList: list) -> str:
        # returns input list but in the form of a string
        return str(inputList)
    
    def parens(self, inputTuple: tuple) -> str:
        # returns input tuple but in the form of a string
        return str(inputTuple)
    
    # def notty(self, data) -> str:
    #     # returns input with not in front of it
    #     return self.__postpre('!', data)
        
    def notEq(self, field: str, number: int) -> str:
    # Used for not equal. Sample output: 'field != number'
        return self.__filterTrans(field, number, '!=')
    
    def search(self, searchTerm: str) -> str:
        # returns 'search "searchTerm";'
        k =  self.__command('search', self.__slashName(searchTerm))
        print(k)
        return k
    
    def sort(self, field: str, sortKind: str) -> str:
        return self.__command('sort', (field + ' ' + sortKind))
        
    def exclude(self, *fields: str):
        return self.__command('exclude', fields)

    def offset(self, num: int) -> str:
        # returns 'offset = num;'
        return self.__command('offset', str(num))

    def squiggle(self, inputSet: set) -> str:
        # returns input set but in the form of a string
        return str(inputSet)