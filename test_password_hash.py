import time

import pytest
import requests

import conftest

@pytest.mark.skip
def test_password_hash():
    params = {
        'password': 'Jumpcloud1'
    }


    res_code_post = conftest.post_request(params)
    assert res_code_post.status_code == 200
    if res_code_post.text:
        print("\nTest Passed: Job identifier is returned successfully")

    res_code_get = conftest.get_request(res_code_post.text)
    assert res_code_get.status_code == 200
    if res_code_get.text:
        print("\nTest Passed: GET is successful, and password hash is been returned")

    assert conftest.test_password_dict['Jumpcloud1'] == res_code_get.text
    print("\nTest Passed : Password hash is computed as expected")

@pytest.mark.skip
def test_password_with_specialchars():
    params = {
        'password': 'ABtduytwdgjd823748236865##$@$#$%#khskjdhksdn,msdn,m/?><'
    }


    res_code_post = conftest.post_request(params)
    assert res_code_post.status_code == 200

    res_code_get = conftest.get_request(res_code_post.text)
    assert res_code_get.status_code == 200

    print("\nTest Passed: Password with special chars is accepted")

@pytest.mark.skip
def test_error_for_empty_password():
    params = {
        'password': ''
    }

    print("Sending empty password string to POST request")
    res_code_post = conftest.post_request(params)
    assert res_code_post.status_code >= 400

    print("\nTest Passed: Error returned for Empty Password string is not allowed")

@pytest.mark.skip
def test_error_for_malformed_input():
    params = {}

    print("Sending Incorrect parameter to POST request")
    res_code_post = conftest.post_request(params)
    assert res_code_post.status_code >= 400

    print("\nTest Passed: Error returned for Incorrect input parameter")

@pytest.mark.skip
def test_error_for_malformed_input_1():
    params = {
        'name': 'Pradnya Deshmukh'
    }

    print("Sending Incorrect parameter to POST request")
    res_code_post = conftest.post_request(params)
    assert res_code_post.status_code >= 400

    print("\nTest Passed: Error returned for Incorrect input parameter")

@pytest.mark.skip
def test_timetaken_to_return_job_identifier():
    params = {
        'password': 'Jumpcloud2'
    }

    start_time = time.time()
    res_code_post = conftest.post_request(params)
    time_taken = time.time() - start_time
    assert res_code_post.status_code == 200

    assert time_taken < 2

    print("\nTest Passed: Job Identifier is returned immediately")

@pytest.mark.skip
def test_app_waits_for_5sec_to_compute_hash():
    params = {
        'password': 'Jumpcloud3'
    }

    start_time = time.time()
    res_code_post = conftest.post_request(params)
    time_taken = time.time() - start_time
    assert res_code_post.status_code == 200

    assert time_taken > 5

    print("\nTest Passed: Application waits for 5 seconds to compute the password hash")

@pytest.mark.skip
def test_error_for_empty_job_id_in_get_request():

    response_code = requests.get(conftest.host_url + conftest.hashurl + '/')
    assert response_code.status_code >= 400
    print("\nTest Passed: Error returned for empty job identifier in GET request")

@pytest.mark.skip
def test_error_for_invalid_job_id_in_get_request():

    response_code = requests.get(conftest.host_url + conftest.hashurl + '/' + '2000')
    assert response_code.status_code >= 400
    print("\nTest Passed: Error returned for job identifier which doesn't exist")

    response_code = requests.get(conftest.host_url + conftest.hashurl + '/' + 'Jumpcloud4')
    assert response_code.status_code >= 400
    print("\nTest Passed: Error returned for invalid job identifier")

@pytest.mark.skip
def test_get_stats():

    response_code = conftest.get_stats()
    assert response_code.status_code == 200
    data = response_code.json()

    if ('TotalRequests' in data and 'AverageTime' in data) :
        print("\nTest Passed: GET Stats returned TotalRequests and AverageTime")


def test_get_stats_TotalRequests_and_AverageTime():
    params = {
        'password': 'Jumpcloud1'
    }

    response_code = conftest.get_stats()
    assert response_code.status_code == 200
    data = response_code.json()
    TotalRequests = data['TotalRequests']

    expected_TotalRequests = TotalRequests + 1

    res_code_post = conftest.post_request(params)
    assert res_code_post.status_code == 200

    response_code = conftest.get_stats()
    assert response_code.status_code == 200
    data = response_code.json()
    Actual_TotalRequests = data['TotalRequests']

    assert Actual_TotalRequests == expected_TotalRequests
    print("\n Test Passed: TotalRequests in GET stats is computed correctly ")

    #Assumption : expected_avg_time is approximately in the range of 5000 - 6000 milliseconds
    assert data['AverageTime'] > 5000 and data['AverageTime'] < 6000
    print("\n Test Passed: TotalRequests in GET stats is computed correctly ")


