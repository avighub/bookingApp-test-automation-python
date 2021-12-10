import json

import requests
from pprint import pprint

from utils import FileReader
from utils.FileReader import read_json_file
import conftest


def test_create_new_booking_withJsonText_and_verify_booking_info():
    # Preparation
    baseUrl = "https://restful-booker.herokuapp.com/booking"
    # Python String
    createBooking_req_body = {
        "firstname": "Deepa",
        "lastname": "Seeba",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    # Converting to JSON String
    createBooking_req_body_json = json.dumps(createBooking_req_body)
    pprint(createBooking_req_body_json)

    # Action
    response_createBooking = requests.post(baseUrl, createBooking_req_body_json,
                                           headers={"Content-Type": "application/json"})

    # Debug
    # REQUEST
    print("\nREQUEST URL: " + response_createBooking.request.url)
    print("REQUEST BODY: " + response_createBooking.request.body)
    print("REQUEST HEADERS:")
    print(response_createBooking.request.headers)
    # RESPONSE
    print("RESPONSE BODY:")
    response_createBooking_json = response_createBooking.json()
    pprint(json.dumps(response_createBooking_json))

    # Assertion
    # Using Default Python assertion
    assert response_createBooking.status_code == 200
    bookingId = response_createBooking_json["bookingid"]
    print("BOOKING ID")
    print(bookingId)
    assert response_createBooking_json["booking"]["firstname"] == "Deepa"
    assert response_createBooking_json["booking"]["lastname"] == "Seeba"


def test_create_new_booking_with_jsonFile_and_verify_booking_info():
    # Preparation
    # Reading BASE_URI from conftest module

    headers = {"Content-Type": "application/json"}

    # Reading JSON from File
    createBooking_req_body = read_json_file("createBookingRequest.json")
    # Printing JSON String
    pprint(createBooking_req_body)
    # Converting to JSON Object
    createBooking_req_body_json = json.dumps(createBooking_req_body)
    pprint(createBooking_req_body_json)

    # Action
    response_createBooking = requests.post(url=BASE_URI, data=createBooking_req_body_json,
                                           headers=headers)

    # Debug
    print("\nREQUEST URL: " + response_createBooking.request.url)
    print("REQUEST BODY: " + response_createBooking.request.body)
    print("\nREQUEST Headers: ")
    print(response_createBooking.request.headers)
    print("RESPONSE BODY:")
    pprint(response_createBooking.json())

    # Assertion
    assert response_createBooking.status_code == 200
    response_createBooking_json = response_createBooking.json()
    assert response_createBooking_json["booking"]["firstname"] == "Deepa"


# Removing all PRINT statements
def test_create_new_booking_with_jsonFile_and_verify_booking_info_updated():
    # Preparation
    headers = {"Content-Type": "application/json"}

    # Reading JSON from File
    createBooking_req_body = FileReader.read_json_file("createBookingRequest.json")

    # Action
    response_createBooking = requests.post(url=conftest.BASE_URI, data=json.dumps(createBooking_req_body),
                                           headers=headers)

    # Assertion
    assert response_createBooking.status_code == 200
    assert response_createBooking.json()["booking"]["firstname"] == "Deepa"

# # get call to validate
# url_get = f'{baseUrl}/{bookingId}'
# print(url_get)
# response_getBooking = requests.get(url_get).json()
# pprint(response_getBooking)
# assert response_getBooking["firstname"] == "Deepa"
