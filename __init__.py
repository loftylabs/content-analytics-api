import requests

from contentanalytics.models import Product


class Api(object):

    def __init__(self, url, access_token=None):
        self.url = url
        self.headers = {
            'Authorization': f'Token {access_token}',
        }

    def get_product_lists(self, *args, **kwargs):
        api_path = 'product_lists'
        r_json = requests.get(self.url + api_path, headers=self.headers, params=kwargs).json()
        return [Product(**product) for product in r_json['results']]

    def get_search_term_groups(self, *args, **kwargs):
        api_path = 'search_term_groups'
        r = requests.get(self.url + api_path, headers=self.headers, params=kwargs)
        return r.json()

    def get_search_terms(self, *args, **kwargs):
        api_path = 'search_terms'
        r = requests.get(self.url + api_path, headers=self.headers, params=kwargs)
        return r.json()

    def get_sites(self, *args, **kwargs):
        api_path = 'sites'
        r = requests.get(self.url + api_path, headers=self.headers, params=kwargs)
        return r.json()

    def get_brands(self, *args, **kwargs):
        api_path = 'brands'
        r = requests.get(self.url + api_path, headers=self.headers, params=kwargs)
        return r.json()

    def get_dates(self, *args, **kwargs):
        api_path = 'dates'
        r = requests.get(self.url + api_path, headers=self.headers, params=kwargs)
        return r.json()

    def get_price_data(self, date, search_term_group_id=None, search_term_id=None, product_list_id=None, *args, **kwargs):
        params = {
            'date': date,
            'search_term_group_id': search_term_group_id,
            'search_term_id': search_term_id,
            'product_list_id': product_list_id,
        }

        r = requests.get(self.url + 'price_data', headers=self.headers, params=params)
        return r.json()

    def get_ranking_data(self, *args, **kwargs):
        api_path = 'ranking_data'
        r = requests.get(self.url + api_path, headers=self.headers, params=kwargs)
        return r.json()

    def get_out_of_stock_data(self, *args, **kwargs):
        api_path = 'out_of_stock_data'
        r = requests.get(self.url + api_path, headers=self.headers, params=kwargs)
        return r.json()

    def get_buy_box_data(self, *args, **kwargs):
        api_path = 'buy_box_data'
        r = requests.get(self.url + api_path, headers=self.headers, params=kwargs)
        return r.json()

    def get_reviews_data(self, *args, **kwargs):
        api_path = 'reviews_data'
        r = requests.get(self.url + api_path, headers=self.headers, params=kwargs)
        return r.json()
