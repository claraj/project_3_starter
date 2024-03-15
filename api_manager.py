import api_1
import api_2
import api_3

def perform_search(search_term):

    # TODO Add error handling 
    # Change names of api_1 and make_request function to suit your app 

    result_1 = api_1.make_request(search_term)
    result_2 = api_2.make_request(search_term)
    result_3 = api_3.make_request(search_term)

    # Edit this to suit the specific data in your app 
    return [result_1, result_2, result_3]

