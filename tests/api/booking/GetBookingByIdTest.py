import json

import requests

from resuableFunc import CreateBookingFunc
from utils import FileReader
import conftest


def test_Verify_bookingInfo_using_valid_bookingID():
    # Preparation
    # Step 1 - create new booking
    headers = {"Content-Type": "application/json"}
    createBooking_req_body = FileReader.read_json_file("createBookingRequest.json")
    response_createBooking = requests.post(url=conftest.BASE_URI, data=json.dumps(createBooking_req_body),
                                           headers=headers)
    print(response_createBooking.json())
    # Step2 : Extract booking id
    bookingId = response_createBooking.json()["bookingid"]
    print(bookingId)

    # # Execution
    getUrlById = f'{conftest.BASE_URI}/{bookingId}'
    print(getUrlById)
    response_getBooking = requests.get(url=getUrlById)
    print(response_getBooking.json())

    # # Assertion
    assert response_getBooking.status_code == 200
    assert response_getBooking.json()["firstname"] == "Deepa"
    assert response_getBooking.json()["bookingdates"]["checkin"] == "2018-01-01"


def test_Verify_bookingInfo_using_valid_bookingID_improved():
    # Preparation
    # Step1: Extract booking id
    bookingId = CreateBookingFunc.createNewBookingAndReturnValue("bookingid")

    # # Execution
    getUrlById = f'{conftest.BASE_URI}/{bookingId}'
    response_getBooking = requests.get(url=getUrlById)
    print(response_getBooking.json())

    # # Assertion
    assert response_getBooking.status_code == 200
    assert response_getBooking.json()["firstname"] == "Deepa"
    assert response_getBooking.json()["bookingdates"]["checkin"] == "2018-01-01"
