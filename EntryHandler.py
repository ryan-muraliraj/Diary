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

    def create_file(self, message:str) -> bool:
        x = os.path.realpath(os.path.dirname(__file__)) + "\\{NAME}.json".format(NAME = date.today())
        print(x)
        self.path = Path(x)
        if os.path.exists(self.path):
            print("File already exists")
            return False       
        try:
            f = open(self.path, 'w')
            self.json = {'entry' : message}
            print(self.json)
            json.dump(self.json, f)
            f.close()
            return True
        except Exception as ex:
            print(ex)
            return False
        pass      
        

handler = EntryHandler()
handler.create_file("Today I took two quizzes!")
#handler.load_file("2022-01-08")
print(handler.retrieve_message())