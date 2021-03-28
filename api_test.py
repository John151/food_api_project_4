import unittest
from unittest import TestCase
from unittest.mock import patch, call
import yelp_api
from picture_api import request_images
from recipe_api import recipe_call
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


  # Tests if result matches expected result
  def test_matching_image_url(self):
    test_search_term = 'cheesesteak'
    mock_result = 'https://images.unsplash.com/photo-1608744221958-a842da518d01?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMTEyMTJ8MHwxfHNlYXJjaHwxfHxjaGVlc2VzdGVha3xlbnwwfHx8fDE2MTY5MDUxMzg&ixlib=rb-1.2.1&q=80&w=1080' 
    test_search = request_images(test_search_term)
    self.assertEqual(mock_result, test_search)

  # Tests if an incorrect result matches search 
  def test_matching_wrong_image_url(self):
    test_search_term = 'hamburger'
    mock_result = 'https://images.unsplash.com/photo-1608744221958-a842da518d01?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMTEyMTJ8MHwxfHNlYXJjaHwxfHxjaGVlc2VzdGVha3xlbnwwfHx8fDE2MTY5MDUxMzg&ixlib=rb-1.2.1&q=80&w=1080' 
    test_search = request_images(test_search_term)
    self.assertNotEqual(mock_result, test_search)

  # Tests if recipe matches expected result 
  def test_recipe_match(self):
    test_search_term = 'fajitas'
    mock_result = ['Skirt Steak Fajitas', ['2-3 bell peppers, ends trimmed, cored and seeded, cut into a couple large pieces', '2 T. brown sugar', '1/3 c. canola oil', '1 t. chile powder', 'cilantro', '1 t. cumin', '18 6-inch flour tortillas', '1 clove of garlic, peeled and finely chopped', '1/3 c. fresh squeezed lime juice', 'lime wedges', 'salsa', 'about 2 lb. skirt steak', 'sour cream', '1/3 c. soy sauce', '1 large white onion, peeled and cut into 1/2-3/4-inch slices (keep the slices intact)'], ['Whisk together the marinade ingredients in a small bowl. Reserve about 1/3 cup of marinade for the vegetables.', 'Place the steak in a gallon-sized ziplock bag.', 'Add the remaining marinade. Seal the bag, pressing out any excess air, massage the marinade into the meat a bit. Refrigerate anywhere from 3-10 hours.After meat has finished marinating, remove steak from marinade and wipe off excess marinade with paper towel. (I also cut the steak into a couple of more manageable sized pieces, for easier turning on the grill). brush the vegetables with reserved marinade.', 'Heat your grill to high. Scrape the grill grate clean and oil the grate.', 'Add the steak to the super hot grill and grill, covered about 2 1/2 minutes per side (for medium/medium-rare), or until steak reaches desired doneness.', 'Remove steak to a clean plate and cover with foil &amp; let rest for 10-15 minutes.', 'Add the peppers and onions to the grill and grill, turning occasionally until cooked, peppers should take about 5 minutes and onions will take about 1', 'Remove from grill. Briefly add the tortillas to the grill, a couple at a time and grill until warmed and lightly charred around the edges. Wrap the tortillas in foil to keep warm.Thinly slice the steak, against the grain. Slice the onions in half and separate the rings. Slice the peppers.', 'Serve with the tortillas, lime wedges and toppings of your choice.']]
    test_search = recipe_call(test_search_term)
    self.assertEqual(mock_result, test_search)
    print(5)

  # Tests if an incorrect result matches search 
  def test_recipe_no_match(self):
    test_search_term = 'chicken wings'
    mock_result = ['Skirt Steak Fajitas', ['2-3 bell peppers, ends trimmed, cored and seeded, cut into a couple large pieces', '2 T. brown sugar', '1/3 c. canola oil', '1 t. chile powder', 'cilantro', '1 t. cumin', '18 6-inch flour tortillas', '1 clove of garlic, peeled and finely chopped', '1/3 c. fresh squeezed lime juice', 'lime wedges', 'salsa', 'about 2 lb. skirt steak', 'sour cream', '1/3 c. soy sauce', '1 large white onion, peeled and cut into 1/2-3/4-inch slices (keep the slices intact)'], ['Whisk together the marinade ingredients in a small bowl. Reserve about 1/3 cup of marinade for the vegetables.', 'Place the steak in a gallon-sized ziplock bag.', 'Add the remaining marinade. Seal the bag, pressing out any excess air, massage the marinade into the meat a bit. Refrigerate anywhere from 3-10 hours.After meat has finished marinating, remove steak from marinade and wipe off excess marinade with paper towel. (I also cut the steak into a couple of more manageable sized pieces, for easier turning on the grill). brush the vegetables with reserved marinade.', 'Heat your grill to high. Scrape the grill grate clean and oil the grate.', 'Add the steak to the super hot grill and grill, covered about 2 1/2 minutes per side (for medium/medium-rare), or until steak reaches desired doneness.', 'Remove steak to a clean plate and cover with foil &amp; let rest for 10-15 minutes.', 'Add the peppers and onions to the grill and grill, turning occasionally until cooked, peppers should take about 5 minutes and onions will take about 1', 'Remove from grill. Briefly add the tortillas to the grill, a couple at a time and grill until warmed and lightly charred around the edges. Wrap the tortillas in foil to keep warm.Thinly slice the steak, against the grain. Slice the onions in half and separate the rings. Slice the peppers.', 'Serve with the tortillas, lime wedges and toppings of your choice.']]
    test_search = recipe_call(test_search_term)
    print(6)
    self.assertNotEqual(mock_result, test_search)
    
if __name__ == '__main__':
  unittest.main()