import pickle

f = open('data.pickle', 'rb')
data = pickle.load(f)
print(data)