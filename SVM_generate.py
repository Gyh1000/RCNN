import keras.models

from sklearn import svm
from parse import parse
from sklearn import pipeline
from sklearn.preprocessing import MinMaxScaler
from joblib import dump, load
import load_data
from imblearn.over_sampling import SMOTE





# some tips
# from joblib import dump, load
# dump(clf, 'filename.joblib')
def SVM_generate(train,label):
    arg=parse()
    SVM_C = arg.SVM_c
    SVM_kernal = arg.SVM_kernal
    SVM_degree = arg.SVM_degree
    SVM_gamma = arg.SVM_gamma
    # coef0 = 0.0
    # shrinking = True
    # probability = False
    # tol = 0.001
    # cache_size = 200
    # class_weight = None
    # verbose = False
    # max_iter = -1
    # decision_function_shape = 'ovr'
    # break_ties = False
    # random_state = None
    # clf = svm.SVC(C=SVM_C,kernel=SVM_kernal,gamma=SVM_gamma,degree=SVM_degree)
    pipe=pipeline.Pipeline([('scaler', MinMaxScaler()),
                            ('svc', svm.SVC(C=SVM_C,
                                            kernel=SVM_kernal,
                                            gamma=SVM_gamma,
                                            degree=SVM_degree)
                             )
                            ])
    pipe.fit(train,label)
    return pipe




def generate(train,label,name):
    clf=SVM_generate(train,label)
    dump(clf,"SVM_model/"+name+'.joblib')



def generate_all():
    #load train_data
    #load result from neural network
    #generate n SVM and save
    arg=parse()
    model_name=arg.CNN_model_name
    model=keras.models.load_model("CNN_model/"+model_name)
    train,label_train=load_data.load_train()


    x=model.predict(train)
    y=label_train

    label=load_data.number_corresponding_label()
    for name in label:
        x_train,y_train=generate_train_data(x,y,name)
        generate(x_train,y_train,name)




def generate_train_data(x,y,name):
    #using smote
    arg=parse()
    x_processed, y_processed=label_train_data(x,y,name)
    smote=SMOTE(random_state=arg.random_seed)
    x_train,y_train=smote.fit_resample(x_processed,y_processed)
    return x_train,y_train




def label_train_data(x,y,name):
    # label = load_data.number_corresponding_label()
    y_processed=[]

    for lab in y:
        if name==lab:
            y_processed.append(1)
        else:
            y_processed.append(0)


    return x,y_processed




def load_generated_SVM_modal():
    #load all SVM
    label = load_data.number_corresponding_label()
    i=0
    clf=[]
    clf.append(i)
    for name in label:
        clf.append(i)
        clf[i] = load('SVM_model/'+name+'.joblib')
        i=i+1
        # clf.append(i)

    return clf

if __name__=='__main__':
    generate_all()