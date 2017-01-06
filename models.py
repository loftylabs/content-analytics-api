import json


class ContentAnalyticsModel(object):

    def __init__(self):
        self.param_defaults = {}

    def __str__(self):
        return json.dumps(self.as_dict(), sort_keys=True)

    def __repr__(self):
        return json.dumps(self.as_dict(), sort_keys=True)

    def as_dict(self):
        data = {}

        for key, value in self.param_defaults.items():
            if getattr(self, key, None):
                data[key] = getattr(self, key, None)
        return data


class Product(ContentAnalyticsModel):

    def __init__(self, *args, **kwargs):
        super().__init__()

        self.param_defaults = {
            'crawl': None,
            'crawl_frequency': None,
            'created_at': None,
            'id': None,
            'ignore_variant_data': None,
            'is_custom_filter': None,
            'is_public': None,
            'name': None,
            'type': None,
            'urgent': None,
            'user_id': None,
            'with_price': None,
        }

        for param, default in self.param_defaults.items():
            setattr(self, param, kwargs.get(param, default))


class SearchTermGroup(ContentAnalyticsModel):

    def __init__(self, *args, **kwargs):
        super().__init__()

        self.param_defaults = {
            'created_at': None,
            'enabled': None,
            'id': None,
            'name': None,
        }

        for param, default in self.param_defaults.items():
            setattr(self, param, kwargs.get(param, default))


class SearchTerm(ContentAnalyticsModel):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.param_defaults = {
            'group_id': None,
            'id': None,
            'title': None
        }

        for param, default in self.param_defaults.items():
            setattr(self, param, kwargs.get(param, default))


class Sites(ContentAnalyticsModel):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.param_defaults = {
            'crawler_name': None,
            'id': None,
            'image_url': None,
            'location': None,
            'name': None,
            'results_per_page': None,
            'site_type': None,
            'traffic_upload': None,
            'url': None,
            'user_agent': None,
            'zip_code': None,
        }

        for param, default in self.param_defaults.items():
            setattr(self, param, kwargs.get(param, default))


class Brand(ContentAnalyticsModel):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.param_defaults = {
            'brand_type': None,
            'company_id': None,
            'created': None,
            'id': None,
            'name': None,
            'parent_id': None,
        }

        for param, default in self.param_defaults.items():
            setattr(self, param, kwargs.get(param, default))


class Date(ContentAnalyticsModel):
    pass


class PriceData(ContentAnalyticsModel):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.param_defaults = {
            'url': None,
            'title': None,
            'currency': None,
            'price': None,
        }

        for param, default in self.param_defaults.items():
            setattr(self, param, kwargs.get(param, default))


class RankingData(ContentAnalyticsModel):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.param_defaults = {
            'search_term': None,
            'site_id': None,
            'title': None,
            'url': None,
            'ranking': None,
        }

        for param, default in self.param_defaults.items():
            setattr(self, param, kwargs.get(param, default))


class OutOfStockData(ContentAnalyticsModel):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.param_defaults = {
            'search_term': None,
            'site_id': None,
            'title': None,
            'url': None,
            'is_out_of_stock': None,
            'no_longer_available': None,
        }

        for param, default in self.param_defaults.items():
            setattr(self, param, kwargs.get(param, default))


class BuyBoxData(ContentAnalyticsModel):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.param_defaults = {
            'search_term': None,
            'site_id': None,
            'title': None,
            'marketplace': None,
            'url': None,
            'is_out_of_stock': None,
            'no_longer_available': None,
            'first_party_owned': None,
        }

        for param, default in self.param_defaults.items():
            setattr(self, param, kwargs.get(param, default))


class ReviewsData(ContentAnalyticsModel):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.param_defaults = {
            'search_term': None,
            'site_id': None,
            'title': None,
            'total_count': None,
            'average_num': None,
            'one_star': None,
            'two_star': None,
            'three_star': None,
            'four_star': None,
            'five_star': None,
        }

        for param, default in self.param_defaults.items():
            setattr(self, param, kwargs.get(param, default))
