from tensorflow.python.keras.layers import Layer
class FM(Layer):
    """
    实现
    """
    def __init__(self, **kwargs):
        super(FM, self).__init__(kwargs)

    def build(self, input_shape):
        if len(input_shape)!=3:
            raise ValueError("input shape should be 3")

        super(FM, self).build(input_shape)

    def call(self, inputs):

        return