### Test Automation Summary
The Automation Test Suite is been created using Pytest framework. 
Below are the Test scripts and their brief description :

a.	Conftest.py – This file holds the global variables and common modules used across the other test scripts

b.	Test_password_hash.py – This file includes various test modules corresponding to test cases documented in Test case template. I have tried to match the module names to the test cases.

c.	Test_async_POST_requests.py – This program is to test multiple POST request sent asynchronously. This is not fully functional and getting into runtime erros. However,  the goal was to test programmatically whether Application is able to handle asynchronous requests successfully. Hope it helps to understand the approach and provides psudo code.

d.	Test_inflight_requests_during_shutdown.py – Attempted to test this functionality programmatically using multiprocessing /process and Queues

e.	Test_error_post_shutdown_request.py - Attempted to test this functionality programmatically using multiprocessing /process and Queues

f.	Report.html – Pytest allows to generate html report giving the summary of automation test execution. (pytest -v test_password_hash.py --html=report.html)

Please note that, I have marked test cases to be skipped (@pytest.mark.skip) which triggers the shutdown to avoid interreference to remaining test execution. However, those can be run individually. 

Assumptions : 
Since the expected and actual password hash is not matching, It is not clear that GET request should return the the base64 encoded password hash for the corresponding password or SHA512 password hash computed in the POST request. Hence assumption is made that application is expected to generate SHA512 password hash after the POST request. Then for GET request -  It’ll return base64 encoded password hash of the SHA512 password hash.
