import json
from typing import List

#region functions

def convertToDict(data: List[str]) -> dict:
    return dict() if len(data) == 0 else json.loads(data)

def saveToFile(passDict):
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

def addOrUpdateAccInfo(passDict): 
    key = input("\nEnter key: ")
    accUsername = input("Enter account username: ")
    accPassword = input("Enter account password: ")


    if key in passDict.keys():
        print(f"\nKey '{key}' already exists.")
        answer = 0
        while answer not in [1,2]:
            try: 
                answer = int(input("Do you want to update it? 1) Yes 2) No\n"))
            except: 
                print("Invalid input.")
            else: 
                if answer not in [1,2]:
                    return print("Invalid option.")
                if answer == 2: return print(f"No changes applied.")
                if answer == 1: 
                    passDict[key]['username'] = accUsername
                    passDict[key]['password'] = accPassword
                    saveToFile(passDict)
                    return print(f"Account info for key '{key}' has been updated.")
    passDict[key] = dict()
    passDict[key]['username'] = accUsername
    passDict[key]['password'] = accPassword
    saveToFile(passDict)
    return print(f"Account info for key '{key}' has been added.")
    
def getAccInfo(passDict):
    key = input("\nEnter key: ")
    if key not in passDict.keys():
        return print(f"Key '{key}' does not exist.")
    return print(f"Account info for key '{key} is:\nUsername: '{passDict[key]['username']}'\nPassword: '{passDict[key]['password']}'")

def deleteAccInfo(passDict):
    key = input("Enter key: ")
    if key not in passDict.keys():
        return print(f"Key '{key}' does not exist.")
    passDict.pop(key)
    saveToFile(passDict)
    print(f"Key '{key}' and its information have been removed.")
    return

def getAllKeys(passDict: dict):

    if len(passDict) == 0:
        return print("Collection is empty.")
    print("\nAvailable keys:")
    for key in passDict: 
        print(f'   - {key}')

#endregion

menu_functions = {
    1: addOrUpdateAccInfo,
    2: getAccInfo,
    3: deleteAccInfo,
    4: getAllKeys
}

def main():
    global filename
    filename = ""
    fileObj = None
    try:
        filename = input("Name of txt file: ").strip()
        fileObj = open(f"{filename}.txt",'r')
        print("\nCollection loaded.")

    except FileNotFoundError as err : 
        fileCreate = open(f"{filename}.txt",'w')
        fileCreate.close()
        fileObj = open(f"{filename}.txt",'r')
        print("\nCollection created.")

    passDict = dict()
    try: 
        passDict = convertToDict(fileObj.read())  
    except: 
        print(f"Error! Problem with reading from file '{filename}.txt'.") 
        return
    finally: 
        fileObj.close()
    print("App started.")
    if len(passDict) > 0: 
        getAllKeys(passDict)
    inp = ""
    while inp != "exit":
        print("\nChoose an option.")
        option = 0
        optionsStr = [1,2,3,4]
        options = { 
            1: 'Add new account info or update existing',
            2: 'Get account info for a key',
            3: 'Delete key and account info',
            4: 'Get all keys'
        }
        while option not in options.keys():
            try:
                index = 1
                for key in options:
                    print(f'   {index}) {options[key]}')
                    index += 1
                option = int(input("\nChoose one number: "))
                inp = str(option)
            except:
                print(f'Please input numbers', optionsStr, 'only.')
                inp = ""
                break
            
            if option not in options.keys():
                print("Invalid option.")
                inp = ""
                continue
        if inp == "": 
            continue
        try: 
            menu_functions[option](passDict)
        except Exception as err:
            print(err)
        
        inp = input("\nPress any key to continue or  type 'exit' to close the app.\n")
    # try: 
    #     saveToFile(passDict,filename)
    # except Exception as err: 
    #     print(err)

if __name__ == '__main__':
    main()