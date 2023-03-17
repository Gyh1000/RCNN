import argparse

def parse():
    parse=argparse.ArgumentParser()
    parse.add_argument('--image_size',
                       dest='image_size',
                       type=int,
                       default=50,
                       help='This specify the smallest image size.')


    parse.add_argument('--image_number',
                       dest='image_number',
                       type=int,
                       default=50,
                       help='This specify the number of the sub_image.')

    parse.add_argument('--SVM_c',
                       dest='SVM_c',
                       type=float,
                       default=1.0,
                       help='This specify the SVM C parameter.')

    parse.add_argument('--SVM_kernel',
                       dest='SVM_kernal',
                       type=str,
                       default='rbf',
                       help='This specify the SVM kernal parameter.')

    parse.add_argument('--SVM_degree',
                       dest='SVM_degree',
                       type=int,
                       default=3,
                       help='This specify the SVM degree parameter.')

    parse.add_argument('--SVM_gamma',
                       dest='SVM_gamma',
                       type=str,
                       default='scale',
                       help='This specify the SVM gamma parameter.')
    # kernel = 'rbf'
    # degree = 3
    # gamma = 'scale'
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

    parse.add_argument('--epoch',
                       dest='epoch',
                       default=200,
                       type=int,
                       help='This is epoch')

    parse.add_argument('--learning_rate',
                       default=0.1,
                       dest='learning_rate',
                       type=float,
                       help='This is learning_rate')

    parse.add_argument('--seed',
                       default=116,
                       dest='random_seed',
                       type=int,
                       help='This is random_seed')

    parse.add_argument('--validation_split',
                       dest='validation_split',
                       default=0.2,
                       type=float,
                       help='This is validation_split')

    parse.add_argument('--validation_frequence',
                       dest='validation_frequence',
                       default=5,
                       type=int,
                       help='This is validation_frequence')

    parse.add_argument('--batch_size',
                       dest='batch_size',
                       default=32,
                       type=int,
                       help='This is batch size')

    parse.add_argument('--show_model',
                       dest='show_model',
                       default=0,
                       type=int,
                       help='This controls if show model structure')

    parse.add_argument('--CNN_model_name',
                       dest='CNN_model_name',
                       type=str,
                       default='image_detection',
                       help='This specify the CNN_model_name.')

    parse.add_argument('--threshold',
                       dest='threshold',
                       default=0.5,
                       type=float,
                       help='This specify the threshold in picture.')


    arg=parse.parse_args()

    return arg

if __name__=='__main__':
    parse()