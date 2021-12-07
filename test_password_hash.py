import time
import pytest
import requests
import conftest


def test_password_hash():
#Test scenarios : 1. POST is successful
#                 2. GET is successful
#                 3. Password Hash is computed correctly

    res_code_post = conftest.post_request('Jumpcloud1')
    assert res_code_post.status_code == 200
    if res_code_post.text:
        print("\nTest Passed: Job identifier is returned successfully")

    res_code_get = conftest.get_request(res_code_post.text)
    assert res_code_get.status_code == 200
    if res_code_get.text:
        print("\nTest Passed: GET is successful, and password hash is been returned")

    assert conftest.test_password_dict['Jumpcloud1'] == res_code_get.text
    print("\nTest Passed : Password hash is computed as expected")


def test_password_with_specialchars():
#Negative Test Case : Password with special chars

    password = 'ABtduytwdgjd823748236865##$@$#$%#khskjdhksdn,msdn,m/?><'


    res_code_post = conftest.post_request(password)
    assert res_code_post.status_code == 200

    res_code_get = conftest.get_request(res_code_post.text)
    assert res_code_get.status_code == 200

    print("\nTest Passed: Password with special chars is accepted")


def test_error_for_empty_password():
#Negative Test Case : Empty password in POST

    password = ''

    print("Sending empty password string to POST request")
    res_code_post = conftest.post_request(password)
    assert res_code_post.status_code >= 400

    print("\nTest Passed: Error returned for Empty Password string is not allowed")


def test_error_for_malformed_input():
#Negative Test Case : Incorrect parameter for POST

    params = {}

    print("Sending Incorrect parameter to POST request")
    res_code_post = conftest.post_request_invalid_params(params)
    assert res_code_post.status_code >= 400

    print("\nTest Passed: Error returned for Incorrect input parameter")


def test_error_for_malformed_input_1():
#Negative Test Case : Incorrect parameter for POST

    params = {
        'name': 'Pradnya Deshmukh'
    }

    print("Sending Incorrect parameter to POST request")
    res_code_post = conftest.post_request_invalid_params(params)
    assert res_code_post.status_code >= 400

    print("\nTest Passed: Error returned for Incorrect input parameter")


def test_timetaken_to_return_job_identifier():
#Test Case : verify whether Job id is returned immediately

    start_time = time.time()
    res_code_post = conftest.post_request('Jumpcloud2')
    time_taken = time.time() - start_time
    assert res_code_post.status_code == 200

    assert time_taken < 2

    print("\nTest Passed: Job Identifier is returned immediately")


def test_app_waits_for_5sec_to_compute_hash():
#Test Case : To verify Application waits for 5 seconds to compute the password hash

    start_time = time.time()
    res_code_post = conftest.post_request('Jumpcloud3')
    time_taken = time.time() - start_time
    assert res_code_post.status_code == 200

    assert time_taken > 5

    print("\nTest Passed: Application waits for 5 seconds to compute the password hash")


def test_error_for_empty_job_id_in_get_request():
#Negative Test Case : Empty job identifier in GET
    response_code = requests.get(conftest.host_url + conftest.hashurl + '/')
    assert response_code.status_code >= 400
    print("\nTest Passed: Error returned for empty job identifier in GET request")


def test_error_for_invalid_job_id_in_get_request():
#Negative Test Case : Invalid job identifier in GET

    response_code = requests.get(conftest.host_url + conftest.hashurl + '/' + '2000')
    assert response_code.status_code >= 400
    print("\nTest Passed: Error returned for job identifier which doesn't exist")

    response_code = requests.get(conftest.host_url + conftest.hashurl + '/' + 'Jumpcloud4')
    assert response_code.status_code >= 400
    print("\nTest Passed: Error returned for invalid job identifier")


def test_get_stats_response():
#Test Case : GET Stats returns TotalRequests and AverageTime

    response_code = conftest.get_stats()
    assert response_code.status_code == 200
    data = response_code.json()

    if ('TotalRequests' in data and 'AverageTime' in data) :
        print("\nTest Passed: GET Stats returned TotalRequests and AverageTime")


def test_get_stats_TotalRequests_and_AverageTime():
#Test Case : Verify TotalRequests and AverageTime in GET stats is computed correctly

    response_code = conftest.get_stats()
    assert response_code.status_code == 200
    data = response_code.json()
    TotalRequests = data['TotalRequests']

    expected_TotalRequests = TotalRequests + 1

    res_code_post = conftest.post_request('Jumpcloud5')
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


def test_password_hash_simultaneous_requests():
# Test Case : Verify application is able to process multiple connections simultaneously.

    password_list = ['Jumpcloud1','Jumpcloud2','Jumpcloud3','Jumpcloud4','Jumpcloud5',
                     'Jumpcloud6', 'Jumpcloud7', 'Jumpcloud8','Jumpcloud9', 'Jumpcloud10'  ]
    job_id = []

    start_time = time.time()

    for password in password_list:

        res_code_post = conftest.post_request(password)
        assert res_code_post.status_code == 200
        job_id.append(res_code_post.text)

    end_time = time.time()
    Total_time = end_time - start_time
    expected_average_time = (Total_time * 1000) / 10

    print(f"\nTotal Time taken to make 10 POST requests is ", Total_time)
    print(f"\nExpected Average Time for a POST requests is ", expected_average_time)

    for id in job_id:
        res_code_get = conftest.get_request(id)
        assert res_code_get.status_code == 200

    print("\n Application is able to handle simultaneous POST and GET requests")

@pytest.mark.skip
def test_shutdown_request_response():
#Test Case : Verify shutdown is successful

    response_code = conftest.shutdown_request()
    assert response_code.status_code == 200
    print("\nShutdown is successful")


@pytest.mark.skip
def test_error_new_request_after_shutdown():
#Test Case :Verify application rejects new password hashing received during the shutdown

    response_code = conftest.shutdown_request()
    assert response_code.status_code == 200
    print("\nShutdown is successful")

    res_code_post = conftest.post_request('Jumpcloud11')
    assert res_code_post.status_code != 200

    print("\nTest Passed: Error returned for the request sent after the shutdown ")