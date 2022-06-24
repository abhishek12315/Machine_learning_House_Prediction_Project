import json
import pickle
import numpy as np

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
    
    with open("./server/artifacts/columns.json", "r") as f: 
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
    
    with open("./server/artifacts/banglore_home_prices_model.pickle", "rb") as f: 
        __model1 = pickle.load(f)
    print("Loading artifacts ...done.") 

def get_estimated_price(location, sqft, bhk, bath): 
    try: 
        loc_index = __data_columns.index(location.lower()) 
    except: 
        loc_index = -1
    
    m = np.zeros(len(__data_columns))
    m[0] = sqft
    m[1] = bath
    m[2] = bhk
    
    if loc_index >= 0: 
        m[loc_index] = 1
    
    return round(__model1.predict([m])[0],2)


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    print(get_estimated_price('Kalhalli', 1000, 3, 3)) # Other Location
    print(get_estimated_price('Ejipura', 1000, 2, 2))  # Other Location
    
    
    