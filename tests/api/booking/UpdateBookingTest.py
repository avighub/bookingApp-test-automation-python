import json

import conftest
from resuableFunc import CreateBookingFunc
import requests

from utils import FileReader


def test_Verify_bookingInfo_can_not_updated_without_token():
    # Preparation
    # Step1: Extract booking id
    bookingId = CreateBookingFunc.createNewBookingAndReturnValue("bookingid")

    # # Execution
    updateUrlById = f'{conftest.BASE_URI}/{bookingId}'
    updateBooking_req_body = FileReader.read_json_file("updateBookingRequest.json")
    headers = {"Content-Type": "application/json", "token": "inavlidabcd123"}
    response_updatedBooking = requests.put(url=updateUrlById, data=json.dumps(updateBooking_req_body), headers=headers)
    print(response_updatedBooking.request.body)
    print(response_updatedBooking.content)

    # # Assertion
    assert response_updatedBooking.status_code == 403
    responseString = response_updatedBooking.content.decode("utf-8")
    assert responseString == "Forbidden"

def test_Verify_bookingInfo_can_not_partially_updated_without_token():
    # Preparation
    # Step1: Extract booking id
    bookingId = CreateBookingFunc.createNewBookingAndReturnValue("bookingid")

    # # Execution
    updateUrlById = f'{conftest.BASE_URI}/{bookingId}'
    updateBooking_req_body = FileReader.read_json_file("partialUpdateBookingRequest.json")
    headers = {"Content-Type": "application/json", "token": "inavlidabcd123"}
    response_updatedBooking = requests.put(url=updateUrlById, data=json.dumps(updateBooking_req_body), headers=headers)
    print(response_updatedBooking.request.body)
    print(response_updatedBooking.content)

    # # Assertion
    assert response_updatedBooking.status_code == 403
    responseString = response_updatedBooking.content.decode("utf-8")
    assert responseString == "Forbidden"