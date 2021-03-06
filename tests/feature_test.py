from deepctr.models import DeepFM
from deepctr.feature_column import SparseFeat, DenseFeat, get_feature_names
import numpy as np
import tensorflow as tf
def test_long_dense_vector():
    #构造特征
    feature_columns = [SparseFeat('user_id', 4, ), SparseFeat('item_id', 5, ), DenseFeat("pic_vec", 5)]
    fixlen_feature_names = get_feature_names(feature_columns)

    #构造样本
    user_id = np.array([[1], [0], [1]])
    item_id = np.array([[3], [2], [1]])
    pic_vec = np.array([[0.1, 0.5, 0.4, 0.3, 0.2], [0.1, 0.5, 0.4, 0.3, 0.2], [0.1, 0.5, 0.4, 0.3, 0.2]])
    label = np.array([1, 0, 1])
    input_dict = {'user_id': user_id, 'item_id': item_id, 'pic_vec': pic_vec}
    model_input = [input_dict[name] for name in fixlen_feature_names]

    #创建模型model
    model = DeepFM(feature_columns, feature_columns[:-1])

   # model.summary()
    #tf.keras.utils.plot_model(model, "test_compu")

    #训练模型
    model.compile('adagrad', 'binary_crossentropy')
    model.fit(model_input, label)

test_long_dense_vector()
