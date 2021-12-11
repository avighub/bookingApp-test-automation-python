import json

import requests
from pprint import pprint

from utils import FileReader
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
    createBooking_req_body = FileReader.read_json_file("createBookingRequest.json")
    # Printing JSON String
    pprint(createBooking_req_body)
    # Converting to JSON Object
    createBooking_req_body_json = json.dumps(createBooking_req_body)
    pprint(createBooking_req_body_json)

    # Action
    response_createBooking = requests.post(url=conftest.BASE_URI, data=createBooking_req_body_json,
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
def test_JIRA_001_create_new_booking_with_jsonFile_and_verify_booking_info_updated():
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


# Removing all PRINT statements
def test_create_new_booking_with_jsonFile_with_noHeaders():
    # Preparation
    createBooking_req_body = FileReader.read_json_file("createBookingRequest.json")

    # Action
    response_createBooking = requests.post(url=conftest.BASE_URI, data=json.dumps(createBooking_req_body))

    # Assertion
    responseString = response_createBooking.content.decode("utf-8")
    assert response_createBooking.status_code == 400
    assert responseString == "Bad Request"


def test_create_new_booking_with_header_as_application_xml():
    # Preparation
    headers = {"Content-Type": "application/xml"}
    createBooking_req_body = FileReader.read_json_file("createBookingRequest.json")

    # Execution
    response = requests.post(url=conftest.BASE_URI, headers=headers, data=json.dumps(createBooking_req_body))

    # Assertion
    assert response.status_code == 400
    responseString = response.content.decode("utf-8")
    assert responseString == "Bad Request"
