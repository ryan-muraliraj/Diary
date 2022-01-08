import os, json, time
from pathlib import Path
from datetime import *

class EntryHandler():

    def __init__(self) -> None:
        self.json = ""
        self.message = ""
        pass

    def load_file(self, filename:str) -> None:
        x = os.path.realpath(os.path.dirname(__file__)) + "\\{NAME}.json".format(NAME = filename)
        print(x)
        self.path = Path(x)
        if os.path.exists(self.path) and self.path.suffix == '.json':
            try:
                f = open(self.path, 'r')
                obj = json.load(f)
                self.json = obj
                self.message = obj['entry']
                print(self.json)
                f.close()
            except Exception as ex:
                print("Error " + ex)
        else:
            print("Error")
        
        pass

    def retrieve_message(self) -> None:
        return self.message

    def create_file(self, message:str) -> str:
        x = os.path.realpath(os.path.dirname(__file__)) + "\\{NAME}.json".format(NAME = date.today())
        print(x)
        self.path = Path(x)
        if os.path.exists(self.path):
            print("File already exists")
            return "Error"       
        try:
            f = open(self.path, 'w')
            self.json = {'entry' : message}
            print(self.json)
            json.dump(self.json, f)
            f.close()
            return "Success"
        except Exception as ex:
            print(ex)
            return "Error"
        pass      
        

handler = EntryHandler()
handler.create_file("WOOOOOOOO")
#print(handler.retrieve_message())