import json

import conftest
from utils import FileReader
import requests


def createNewBookingAndReturnValue(filedName):
    headers = {"Content-Type": "application/json"}
    createBooking_req_body = FileReader.read_json_file("createBookingRequest.json")
    response_createBooking = requests.post(url=conftest.BASE_URI, data=json.dumps(createBooking_req_body),
                                           headers=headers)
    value = response_createBooking.json()[filedName]
    return value


def createNewBookingAndReturnResponse():
    headers = {"Content-Type": "application/json"}
    createBooking_req_body = FileReader.read_json_file("../tests/api/booking/createBookingRequest.json")
    response_createBooking = requests.post(url=conftest.BASE_URI, data=json.dumps(createBooking_req_body),
                                           headers=headers)
    return response_createBooking
