import sys
import json

def getArgs():
    print("In here boyoyoyoy")
    if len(sys.argv) > 1:
        temp = sys.argv[1:]
        print(temp)

        temp = ''.join(temp).replace("'","").replace('{', '{"').replace(':','": "').replace(',','", "').replace('}','"}')
        print(json.loads(temp))

        address_list = json.loads(temp)
        for key, value in address_list.items():
            print(f"key: {key}, value: {value}")

        print("watatata")
    else:
        print("No message passed")

getArgs()
