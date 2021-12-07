import requests

#URL formations
host_url = "http://127.0.0.1:8088/"
hashurl = 'hash'
stats = 'stats'
body = 'shutdown'
#Dictionary for the password and expected hash, for the comparison in the test scripts
test_password_dict = {
    'Jumpcloud1': 'ZTVjYmUyYjJkOThiOWY4NjU4Y2JkNzE3OWRiMTRlZmViYzk3OTY5M2VkN2Q3MGM2NTQ0MjlhMDllYWFjZTNiYmNkMjI2YmE0NWQ4MTRlMzFlOGQ3Nzk4NDQ0OTg0YmVmZjllZjAyNmRmYjhmZjU4NWY2ZWNkYTk4ZGI4MjI3OTE=',
    'Jumpcloud2': 'MWY5YjQ0ZWM0ZDE3MzZhNjcwZjI1MjY1NjY1ZThkZTgwOTE4ZTRhNGQwNmNkNDY0ZTczNzA4NDJhMTU3Y2UzMTBiNDA3MWFiNGI1MTc4Y2YxMWRhNzAzNGQ3N2Y5NWQwMjBiZTdiYmNmMmMxMTAxYTQzOGJmMTI3M2U4NWM3MmQ=',
    'Jumpcloud3': 'NzU4ZWMzYzBjNzBkMGU0OTc5M2E0NjcyMjQ0ZjQzMmM3OGRiOGU0NDA4YTYyZGEyMjkzYjY5ZmEwM2I1NjQwMDZkOTYyOTIyYmY1ZTlhNTI3ZmM2NDRjMDhiZDkxNjczNzg3NTM4Y2MwODZlNWEzNmNhMjdlMmZlZDRkNzc3ZDM=',
    'Jumpcloud4': 'OTdkNTI5ZGMxYmMyNzVmZDQ1ODEzNDQ5Mjg0Y2NhZWQxYWFhZTdmNjgzYmY4ZjkyYjA1MTFjNWYyOTNhMTk2ODNhODdiYjVmMGU0YjZiMGIyYjIwMDBiZTIwNzNmYmMwNGEyMzEyYWFmMmNhYWJhYjQ2NzNmMDg3ZTYyYjgyZmY',
    'ABtduytwdgjd823748236865##$@$#$%#khskjdhksdn,msdn,m/?><': 'ODgxMzE0N2Q1MmI2NmRlNGIxMzQwZGIwNmZmODM4MmQzY2VmMDhmM2MzZmQzMzA3NzY3YTJhMmQ4OWY4Y2I4ZTVmOTMzZDVjOWU2Y2M0ZWQ2NWQ4ZTY3MDBiYmJlYmMzYmMxN2NjYWRhM2MyOGZkM2QzYTQ5MGU1NThmYjgzNmQ='}

# Function to Get the base64 encoded password
def get_request(job_id):
    response_code = requests.get(host_url + hashurl + '/' + job_id)

    print(f"\nThe response code for GET request is :", response_code)
    print(response_code.text)
    return response_code

#Function to Get the stats
def get_stats():
    response_code_stats = requests.get(host_url + stats)
    print(f"\nThe response code for Stats request is :", response_code_stats)
    print(response_code_stats.text)
    return response_code_stats

#Function to Post to the /hash endpoint
def post_request(password):
    params = {
        'password': password
    }
    response_code_post = requests.post(host_url + hashurl, json=params)
    print(f"\nThe response code for POST request is :", response_code_post)
    print(response_code_post.text)
    return response_code_post

#Function to Post to the /hash endpoint with Invalid parameters
def post_request_invalid_params(params):
    response_code_post = requests.post(host_url + hashurl, json=params)
    print(f"\nThe response code for POST request is :", response_code_post)
    print(response_code_post.text)
    return response_code_post

#Function to shutdown the application server
def shutdown_request():
    response_code_shutdown = requests.post(host_url + hashurl, data=body)
    print(f"\nThe response code for Shutdown request is :", response_code_shutdown)
    return response_code_shutdown



