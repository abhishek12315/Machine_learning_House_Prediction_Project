from glob import glob
import json
import pickle

__locations = None      # Global varibles declared double underscore makes it private attribute
__data_columns = None
__model1 = None


def get_location_names():
    return __locations

def load_saved_artifacts():
    print("loading saved artifacts ...start")
    global __data_columns
    global __locations
    global __model1
    
    with open("./artifacts/columns.json", "r") as f: 
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
    
    with open("./artifacts/banglore_home_prices_model.pickle", "rb") as f: 
        __model1 = pickle.load(f)
    print("Loading artifacts ...done.") 
    
if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    