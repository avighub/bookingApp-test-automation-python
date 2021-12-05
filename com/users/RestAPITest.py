import requests


# GET Request
def test_send_get_request_and_verify_status_200_and_page_field_response():
    response = requests.get("https://reqres.in/api/users?page=1")
    assert response.status_code == 200
    response_body = response.json()
    assert "page" in response_body
