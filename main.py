# python3

class Query:
    def __init__(self, number,name):
        self.number = number
        self.name = name

class Tabl:

    def __init__(self):
        self.contacts={}

    def addContact(self,number,name):
        self.contacts[number]=Query(number,name)

    def delContact(self,number):
        if number in self.contacts:
            del self.contacts[number]

    def findContact(self,number):
        if number in self.contacts:
            return self.contacts[number].name
        else:
            return "not found"

def read_queries():
    n = int(input())
    return [input().split() for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    # contacts = []
    hashTable=Tabl()
    for query in queries:
        cur_query = query[0]
        if cur_query == 'add':
            number=int(query[1])
            name=query[2]
            hashTable.addContact(number,name)
        elif cur_query=='del':
            number=int(query[1])
            hashTable.delContact(number)
        else:
            number=int(query[1])
            response=hashTable.findContact(number)
            result.append(response)
    return result
            # if we already have contact with such number,
            # we should rewrite contact's name
if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
