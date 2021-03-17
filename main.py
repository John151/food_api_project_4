from picture_api import request_images
from search_util import prep_search_term
from yelp_api import yelp_call

def main():
    input = prep_search_term('pizza')
    yelp = yelp_call(input)
    sw = prep_search_term(input)
    pic = request_images(sw)
    print(pic)
    print(yelp)

main()
