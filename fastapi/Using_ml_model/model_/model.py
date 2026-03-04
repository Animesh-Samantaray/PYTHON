import pickle
model=""
with open('model_/model.pkl','rb') as f:
    model = pickle.load(f)
    print(model)