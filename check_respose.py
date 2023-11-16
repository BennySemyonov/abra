import requests

def check_response(url):
    try:
        # Make a GET request to the specified URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Assuming the response is JSON, you can parse it
            json_response = response.json()

            # Check if the expected key-value pair is present in the JSON object
            expected_response = {'hello': 'world'}
            if json_response == expected_response:
                print(f"Success! Received the expected response: {json_response}")
            else:
                print(f"Unexpected response format: {json_response}")
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace the URL with your Flask app's URL
    api_url = "http://0.0.0.0:8080"
    check_response(api_url)