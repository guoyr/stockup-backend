from datetime import datetime
import json

from tornado import gen

from config import datetime_repr
from constants import CUR_PRICE, DATE, TIME
from request_handlers.base_request_handler import BaseRequestHandler


class ConditionHandler(BaseRequestHandler):

    @gen.coroutine
    def get(self, condition=None):
        if condition == "price":
            yield self.get_price()
        elif condition == "macd":
            print("macd")
        elif condition == "kdj":
            print ("kdj")

    @gen.coroutine
    def get_price(self):
        """
        :arg:
            start_time: the start time of the query in ISO 8601 format without timezone
            end_time: the end time of the query in the same format
            stock_ids: list of comma separated stock_id to be queried

        :return:
        """
        # TODO: add interval param to only get a a result every x seconds
        start_time_raw = self.get_argument('start_time', None)
        end_time_raw = self.get_argument('end_time', None)
        ids_raw = self.get_argument('stock_ids', None)
        if not (start_time_raw and end_time_raw and ids_raw):
            self.write({'arguments': ['start_time', 'end_time', 'stock_ids']})
            return
        try:
            stock_ids = map(lambda x: int(x), ids_raw.split(','))
            start_time = datetime.strptime(start_time_raw, datetime_repr())
            end_time = datetime.strptime(end_time_raw, datetime_repr())
        except ValueError as e:
            self.write({'error': 'field format incorrect'})
            return

        query = {
            '_id.c': {
                '$in': stock_ids
            },
            '_id.d': {
                '$gte': start_time,
                '$lte': end_time
            }
        }

        if self.get_argument("test", None):
            cursor = self.settings["test_db"].stocks.find(query)
        else:
            cursor = self.settings["db"].stocks.find(query)

        prices_arr = []

        for document in (yield cursor.to_list()):
            a = []
            a.append(document["d"][CUR_PRICE])
            a.append(document["d"][DATE])
            a.append(document["d"][TIME])
            prices_arr.append(a)

        self.write({"d": prices_arr})
