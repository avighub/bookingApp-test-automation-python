import json

import requests
from pprint import pprint
from utils.FileReader import read_json_file


# GET Request
def test_send_get_request_and_verify_status_200_and_page_field_response():
    response = requests.get("https://reqres.in/api/users?page=1")
    assert response.status_code == 200
    response_body = response.json()
    pprint(response_body)
    assert "page" in response_body


def test_create_new_booking_withJsonText_and_verify_booking_info():
    # Preparation
    baseUrl = "https://restful-booker.herokuapp.com/booking"
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
    createBooking_req_body_json = json.dumps(createBooking_req_body)

    # Action
    response_createBooking = requests.post(baseUrl, createBooking_req_body_json,
                                           headers={"Content-Type": "application/json"})

    # Debug
    print("\nREQUEST URL: " + response_createBooking.request.url)
    print("REQUEST BODY: " + response_createBooking.request.body)
    print("\nREQUEST Headers: " + response_createBooking.request.headers.get("Content-Type"))
    print("RESPONSE BODY:")
    pprint(response_createBooking.json())

    # Assertion
    assert response_createBooking.status_code == 200
    response_createBooking_json = response_createBooking.json()
    bookingId = response_createBooking_json.get("bookingid")
    assert response_createBooking_json["booking"]["firstname"] == "Deepa"

    # get call to validate
    url_get = f'{baseUrl}/{bookingId}'
    print(url_get)
    response_getBooking = requests.get(url_get).json()
    pprint(response_getBooking)
    assert response_getBooking["firstname"] == "Deepa"


def test_create_new_booking_with_jsonFile_and_verify_booking_info():
    # Preparation
    baseUrl = "https://restful-booker.herokuapp.com/booking"
    createBooking_req_body = read_json_file("createBookingRequest.json")
    createBooking_req_body_json = json.dumps(createBooking_req_body)
    pprint(createBooking_req_body_json)

    # Action
    response_createBooking = requests.post(baseUrl, createBooking_req_body_json,
                                           headers={"Content-Type": "application/json"})

    # Debug
    print("\nREQUEST URL: " + response_createBooking.request.url)
    print("REQUEST BODY: " + response_createBooking.request.body)
    print("\nREQUEST Headers: " + response_createBooking.request.headers.get("Content-Type"))
    print("RESPONSE BODY:")
    pprint(response_createBooking.json())

    # Assertion
    assert response_createBooking.status_code == 200
    response_createBooking_json = response_createBooking.json()
    bookingId = response_createBooking_json.get("bookingid")
    assert response_createBooking_json["booking"]["firstname"] == "Deepa"

    # get call to validate
    url_get = f'{baseUrl}/{bookingId}'
    print(url_get)
    response_getBooking = requests.get(url_get).json()
    pprint(response_getBooking)
    assert response_getBooking["firstname"] == "Deepa"
