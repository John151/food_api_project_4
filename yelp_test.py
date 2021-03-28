import unittest
from unittest import TestCase
from unittest.mock import patch, call
import yelp_api
from picture_api import request_images
class TestAPICalls(TestCase):


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

  # Tests if result matches correctly
  @patch('requests.get')
  def test_matching_image_url(self):
    test_search_term = 'cheesesteak'
    mock_result = 'https://images.unsplash.com/photo-1608744221958-a842da518d01?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMTEyMTJ8MHwxfHNlYXJjaHwxfHxjaGVlc2VzdGVha3xlbnwwfHx8fDE2MTY5MDUxMzg&ixlib=rb-1.2.1&q=80&w=1080' 
    test_search = request_images(test_search_term)
    self.assertEqual(mock_result, test_search)
  # Tests if an incorrect result 
  @patch('requests.get')
  def test_matching_image_url(self):
    test_search_term = 'hamburger'
    mock_result = 'https://images.unsplash.com/photo-1608744221958-a842da518d01?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMTEyMTJ8MHwxfHNlYXJjaHwxfHxjaGVlc2VzdGVha3xlbnwwfHx8fDE2MTY5MDUxMzg&ixlib=rb-1.2.1&q=80&w=1080' 
    test_search = request_images(test_search_term)
    self.assertNotEqual(mock_result, test_search)

if __name__ == '__main__':
    unittest.main()