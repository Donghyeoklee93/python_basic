# 1. save python object as pickle
import pickle

data = {
    "goal1" : "push-up 100 times everyday",
    "goal2" : "coding 1 hour everyday"
}

file = open("./myvenv/chapter10/data.pickle", "wb")
pickle.dump(data,file)
file.close()


# 2. take pickle file as python
file = open("./myvenv/chapter10/data.pickle", "rb")
data = pickle.load(file)
print(data)
file.close()