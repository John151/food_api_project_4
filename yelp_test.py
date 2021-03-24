import unittest
from unittest import TestCase
from unittest.mock import patch, call
import yelp_api

class TestYelp(TestCase):


  ##to see if Api response matches restaurant name 
    @patch('requests.get')
    def test_restaurant_name(self, mock_requests_get):
        mock_name = 'Hook Fish & Chicken'
        yelp_api_response = {'businesses': [{'id': 'SfxWIcQdrkhRMv0Op9g2_w', 'alias': 'hook-fish-and-chicken-minneapolis-2', 'name': 'Hook Fish & Chicken', 'image_url': 'https://s3-media4.fl.yelpcdn.com/bphoto/USVwS9swJrcFldlP2DeSUw/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/hook-fish-and-chicken-minneapolis-2?adjust_creative=0bqkHrUR6CD88uFafdKfDg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=0bqkHrUR6CD88uFafdKfDg', 'review_count': 13, 'categories': [{'alias': 'chicken_wings', 'title': 'Chicken Wings'}, {'alias': 'cafes', 'title': 'Cafes'}, {'alias': 'seafood', 'title': 'Seafood'}], 'rating': 3.5, 'coordinates': {'latitude': 44.9482453081281, 'longitude': -93.2824693134912}, 'transactions': ['delivery', 'pickup'], 'price': '$$', 'location': {'address1': '221 W Lake St', 'address2': '', 'address3': '', 'city': 'Minneapolis', 'zip_code': '55408', 'country': 'US', 'state': 'MN', 'display_address': ['221 W Lake St', 'Minneapolis, MN 55408']}, 'phone': '+16122009901', 'display_phone': '(612) 200-9901', 'distance': 2026.6219190399024}]}
        mock_requests_get().json.return_value = yelp_api_response
        name = yelp_api_response['businesses'][0]['name']
        self.assertEqual(mock_name, name)

    ## to see if Api response DOES NOT MATCH restaurant name 
    @patch('requests.get')
    def test_restaurant_name_false(self, mock_requests_get):
        mock_name = 'Afro Deli'
        yelp_api_response = {'businesses': [{'id': 'SfxWIcQdrkhRMv0Op9g2_w', 'alias': 'hook-fish-and-chicken-minneapolis-2', 'name': 'Hook Fish & Chicken', 'image_url': 'https://s3-media4.fl.yelpcdn.com/bphoto/USVwS9swJrcFldlP2DeSUw/o.jpg', 'is_closed': False, 'url': 'https://www.yelp.com/biz/hook-fish-and-chicken-minneapolis-2?adjust_creative=0bqkHrUR6CD88uFafdKfDg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=0bqkHrUR6CD88uFafdKfDg', 'review_count': 13, 'categories': [{'alias': 'chicken_wings', 'title': 'Chicken Wings'}, {'alias': 'cafes', 'title': 'Cafes'}, {'alias': 'seafood', 'title': 'Seafood'}], 'rating': 3.5, 'coordinates': {'latitude': 44.9482453081281, 'longitude': -93.2824693134912}, 'transactions': ['delivery', 'pickup'], 'price': '$$', 'location': {'address1': '221 W Lake St', 'address2': '', 'address3': '', 'city': 'Minneapolis', 'zip_code': '55408', 'country': 'US', 'state': 'MN', 'display_address': ['221 W Lake St', 'Minneapolis, MN 55408']}, 'phone': '+16122009901', 'display_phone': '(612) 200-9901', 'distance': 2026.6219190399024}]}
        mock_requests_get().json.return_value = yelp_api_response
        name = yelp_api_response['businesses'][0]['name']
        self.assertNotEqual(mock_name, name)

  

if __name__ == '__main__':
    unittest.main()