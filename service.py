import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from sanic import Sanic, response
from sanic_motor import BaseModel
from offer import seq_size, recommend, prep

app = Sanic(__name__)
app.config.update(dict(REQUEST_TIMEOUT=800, RESPONSE_TIMEOUT=800, MOTOR_URI="mongodb://localhost:27017/sig_platform"))

class Order(BaseModel):
    __coll__ = "orders"
    __unique_fields__ = []

@app.route('/<user>')
async def offer(r, user):
    orders = await Order.get_collection.find(dict(user=user)).sort(('date', -1)).to_list(seq_size)
    orders = sorted(orders, key=lambda o: o['date'])
    orders = prep(orders)
    pr = recommend(orders)
    return response.json(np.argmax(pr, k=10))
