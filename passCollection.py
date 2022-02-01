from io import TextIOWrapper
import json
from typing import List

def convertToDict(data: List[str]) -> dict:
    return dict() if len(data) == 0 else json.loads(data)

def saveToFile(passDict,filename):
    try: 
        fajl = open(f'{filename}.txt','w')
        fajl.write(json.dumps(passDict))
            
    except FileNotFoundError as err:
        raise FileNotFoundError(f"Error! Problem with opening the file '{filename}.txt' ")
    except: 
        raise Exception(f"Error! Problem with writing to file '{filename}.txt'")  
    finally:
        fajl.close()
    return True

def addOrUpdatePassword(passDict): 
    key = input("Enter key: ")
    value = input("Enter value: ")

    if key in passDict.keys():
        print(f"Key '{key}' already exists.")
        answer = 0
        while answer not in [1,2]:
            try: 
                answer = int(input("Do you want to update it? 1)Yes 2)No"))
            except: 
                print("Invalid input")
            else: 
                if answer not in [1,2]:
                    print("Invalid option.")
                elif answer == 1: 
                    passDict[key] = value
                    return print(f"Password for key '{key}' has beend updated")

    passDict[key] = value
    return print(f"Password for key '{key}' has been added.")
    
def getPassword(passDict):
    key = input("Enter key: ")
    if key not in passDict.keys():
        return print(f"Key '{key}' does not exist.")
    return print(f"Password for key '{key} is '{passDict[key]}'")

def deletePassword(passDict):
    key = input("Enter key: ")
    if key not in passDict.keys():
        return print(f"Key '{key}' does not exist.")
    passDict.pop(key)
    print(f"Key '{key}' and its password has been removed.")
    return

def getAllKeys(passDict):
    print("Available keys:")
    for key in passDict: 
        print(f'   - {key}')
func = {
    1: addOrUpdatePassword,
    2: getPassword,
    3: deletePassword,
    4: getAllKeys
}

def main():
    filename = ""
    fileObj = None
    try:
        filename = input("Name of txt file: ").strip()
        fileObj = open(f"{filename}.txt",'r')
    except FileNotFoundError as err : 
        fileCreate = open(f"{filename}.txt",'w')
        fileCreate.close()
        fileObj = open(f"{filename}.txt",'r')

    passDict = dict()
    try: 
        passDict = convertToDict(fileObj.read())  
    except: 
        print(f"Error! Problem with reading from file '{filename}.txt'.") 
        return
    finally: 
        fileObj.close()
    print("Data loaded.")
    print("App started.")
    if len(passDict) > 0: 
        getAllKeys(passDict)
    inp = ""
    while inp != "exit":
        print("Choose an option.")
        option = 0
        options = [1,2,3,4]
        options = { 
            1: 'Add new password or update',
            2: 'Get password for a key',
            3: 'Delete key and password',
            4: 'Get all keys'
        }
        while option not in options.keys():
            try:
                index = 1
                for key in options:
                    print(f'{index}){options[key]}')
                    index += 1
                option = int(input("Choose one number: "))
                inp = str(option)
            except:
                print(f"Please input numbers {options.keys()} only")
                inp = ""
                break
            
            if option not in options.keys():
                print("Invalid option")
                inp = ""
                continue
        if inp == "": 
            continue
        func[option](passDict)
        
        inp = input("Press any key to continue or  type 'exit' to exit\n")
    try: 
        saveToFile(passDict,filename)
    except Exception as err: 
        print(err)

if __name__ == '__main__':
    main()




        
    
