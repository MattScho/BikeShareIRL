import pickle as pkl

'''
Write object to pickle file
'''
def dumpObject(object, fileName:str):
    pkl.dump(object, open(fileName, 'wb+'))

'''
Read object from pickle file
'''
def readObject(fileName:str):
    return pkl.load(open(fileName, 'rb'))