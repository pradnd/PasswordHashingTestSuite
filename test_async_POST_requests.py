import pytest
import time
import asyncio
import aiohttp


host_url = "http://127.0.0.1:8088/"
hashurl = 'hash'
stats = 'stats'
body = 'shutdown'

password_list = ['Jumpcloud1', 'Jumpcloud2', 'Jumpcloud3', 'Jumpcloud4', 'Jumpcloud5']
job_id = []


def get_task(session):
    tasks = []
    for password in password_list:
        params = {
            'password': password
        }

        tasks.append(asyncio.create_task(session.post(host_url + hashurl, json=params, ssl=False)))

        return tasks


async def test_password_hash_async_post_requests():
#Test Case : Verify application is able to process multiple connections simultaneously

    async with aiohttp.ClientSession() as session:
        tasks = get_task(session)
        responses = await asyncio.gather(*tasks)

        for response in responses :
            assert response.status_code == 200
            job_id.append(await response.text)

#Capture start time
start_time = time.time()

asyncio.run(test_password_hash_async_post_requests())

#Capture end time
end_time = time.time()

Total_time = end_time - start_time
expected_average_time = (Total_time * 1000)/ 10

print(f"\nTotal Time taken to make 10 POST requests is ", Total_time)
print(f"\nExpected Average Time for a POST requests is ", expected_average_time)
print("\n Application is able to handle simultaneous POST requests")


