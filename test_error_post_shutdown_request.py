import pytest
import requests
import multiprocessing

host_url = "http://127.0.0.1:8088/"
hashurl = 'hash'
body = 'shutdown'


def shutdown_request_queue(queue):
#Function to work with queue
    response_code_shutdown = requests.post(host_url + hashurl, data=body)
    print(f"\nThe response code for Shutdown request is :", response_code_shutdown)

    queue.put(response_code_shutdown)


def post_request_queue(password, queue):
# Function to work with queue
    params = {
        'password': password
    }
    response_code_post = requests.post(host_url + hashurl, json=params)
    print(f"\nThe response code for POST request is :", response_code_post)
    print(response_code_post.text)
    queue.put(response_code_post)


def put_in_queue(queue):
    queue.put(shutdown_request_queue(queue))


def put_in_queue_post(queue):
    queue.put(post_request_queue(queue))


def test_error_post_shutdown_request():
#Test Case : Verify application rejects new password hashing received during the shutdown

    password = 'Jumpcloud10'
    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=put_in_queue, args=(q,))
    p1.start()

    p2 = multiprocessing.Process(target=put_in_queue_post, args=(password, q,))

    shutdown_res = q.get()
    print(shutdown_res)

    p2.start()
    post_res = q.get()

    assert post_res.status_code != 200

    print("\nTest Passed: Any new request Post Shutdown is rejected")
