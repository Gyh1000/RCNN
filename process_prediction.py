from parse import parse
import numpy as np

def process_prediction(svm_prediction):
    arg=parse()
    threshold=arg.threshold
    i=0
    record=[]
    for list in svm_prediction:
        if max(list)< threshold:
            record.append(i)
        i=i+1

    array=np.array(svm_prediction,dtype=np.float32)
    result=[]
    for i in range(array.shape[0]):
        c = sum(array[i, :])
        c1 = array[i, :] / c
        result.append(c1)
    result = np.array(result, dtype=np.float32)

    # array=np.array(svm_prediction,dtype=np.float32)
    # index=np.argmax(array,axis=0)



    #record中是要删去的序号
    #如果label为-1，则删去框框
    return record,result
