from assertpy import assert_that

import conftest
from resuableFunc import CreateBookingFunc
import requests


def test_Verify_bookingInfo_can_not_be_deleted_without_token():
    # Preparation
    # Step1: Extract booking id
    bookingId = CreateBookingFunc.createNewBookingAndReturnValue("bookingid")

    # # Execution
    deleteUrlById = f'{conftest.BASE_URI}/{bookingId}'
    headers = {"Content-Type": "application/json", "token": "inavlidabcd123"}
    response_deleteBooking = requests.delete(url=deleteUrlById, headers=headers)
    print(response_deleteBooking.content)

    # Python Assertion
    assert response_deleteBooking.status_code == 403
    # assertpy assertion
    assert_that(response_deleteBooking.status_code).is_equal_to(403)

    responseString = response_deleteBooking.content.decode("utf-8")
    # assert responseString == "Forbidden"
    assert_that(responseString).is_equal_to("Forbidden")
