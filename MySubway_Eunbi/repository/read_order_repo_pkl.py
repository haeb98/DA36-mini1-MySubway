import pickle

with open('MySubway/.pkl', 'rb') as f:
    order_data = pickle.load(f)

print(order_data)

