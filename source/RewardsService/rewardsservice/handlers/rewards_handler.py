import json
import tornado.web

from pymongo import MongoClient
from tornado.gen import coroutine

from load_mongo_data import updateCustomerData
from load_mongo_data import returnRewards

class RewardsHandler(tornado.web.RequestHandler):

    @coroutine
    def get(self):
        client = MongoClient("mongodb", 27017)
        db = client["Rewards"]
        rewards = list(db.rewards.find({}, {"_id": 0}))
        self.write(json.dumps(rewards))

class CustomerData(tornado.web.RequestHandler):

    def post(self):
        dict = json.loads(self.request.body.decode("utf-8"))

        email = dict["email"]
        purchase = dict["purchase"]

        rewards = int(purchase)

        updateCustomerData(email, rewards)

class ReturnRewards(tornado.web.RequestHandler):

    def post(self):
        dict = json.loads(self.request.body.decode("utf-8"))

        email = dict["email"]

        rewards = returnRewards(email)

        self.write(rewards)

class RewardMembers(tornado.web.RequestHandler):

    def get(self):
        client = MongoClient("mongodb", 27017)
        db = client["Rewards"]
        rewards = list(db.customer_data.find({}, {"_id": 0}))
        self.write(json.dumps(rewards))