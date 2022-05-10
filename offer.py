import tensorflow as tf
import numpy as np
from pymongo import MongoClient
L, l2 = tf.keras.layers, tf.keras.regularizers.l2
seq_size, pr_magnitude = 64, 1000

# har content ke tavasote user haye ba arzeshe ye kasbokar dide mishan. vasash hazine bar hastan.
# yeki hazine
# oona ke check karde. oona ke kharide.
# each product has a brand
# each product has a category
# each product has a (Repetitive | Popular) name
# each product has a time which seen or bought by a casual user
# dar oon lahze cheghad offer bude rooye product ke neshune user dade shode
# use a text generation to predict next things that probably got bought

def transformer_encoder(inputs, head_size, num_heads, ff_dim, dropout=0):
    x = L.LayerNormalization(epsilon=1e-6)(inputs)
    x = L.MultiHeadAttention(key_dim=head_size, num_heads=num_heads, dropout=dropout)(x, x)
    x = L.Dropout(dropout)(x)
    res = x + inputs
    x = L.LayerNormalization(epsilon=1e-6)(res)
    x = L.Conv1D(filters=ff_dim, kernel_size=1, activation=L.LeakyReLU(alpha=.01))(x)
    x = L.Dropout(dropout)(x)
    x = L.Conv1D(filters=inputs.shape[-1], kernel_size=1)(x)
    return x + res

def build_model(pr_magnitude, input_shapes, head_size, num_heads, ff_dim, num_transformer_blocks, mlp_units, dropout=0, mlp_dropout=0):
    inputs = [L.Input(shape=(seq_size, )) if len(input_shape) == 3 else L.Input(shape=input_shape) for input_shape in input_shapes]
    x = [L.Embedding(round(np.log(input_shape[2]) / np.log(3) * 2), input_shape[0], input_length=input_shape[1])(inputs[i_in]) if len(input_shape) == 3 else inputs[i_in] for i_in, input_shape in enumerate(input_shapes)]
    print(x)
    for _ in range(num_transformer_blocks):
        x = transformer_encoder(x, head_size, num_heads, ff_dim, dropout)
    x = L.GlobalAveragePooling1D(data_format="channels_first")(x)
    for dim in mlp_units:
        x = L.Dense(dim, activation=L.LeakyReLU(alpha=.01))(x)
        x = L.Dropout(mlp_dropout)(x)
    x = L.Dense(pr_space_size, activation="softmax")(x)
    return tf.keras.Model(inputs=inputs, outputs=x)

recomender = build_model(pr_magnitude, ((seq_size , 5, pr_magnitude), (seq_size, 7)), head_size=256, num_heads=4, ff_dim=4, num_transformer_blocks=4, mlp_units=[128], mlp_dropout=0.4, dropout=0.25)

def prep(users):
    pass

def fit(X, y):
    pass

def recommend(x):
    pass

if __name__ == '__main__':
    orders = MongoClient(app.config['MOTOR_URI']).get_database()['orders'].find().sort(('date', '1'))
    users = {}
    for o in orders:
        if o['user'] not in users:
            users[o['user']] = []
        users[o['user']].append(o)
    # make sequences then
    # prep them
    # fit