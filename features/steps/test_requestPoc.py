from behave import given, when, then
import requests

@given('the server is running')
def step_impl(context):
    context.base_url = "http://127.0.0.1:5000"

@when('I request a cat fact')
def step_impl(context):
    context.response = requests.get(f"{context.base_url}/get-cat-fact")

@when('I post a cat fact')
def step_impl(context):
    # Fetch a cat fact first to ensure payload
    fact_response = requests.get("https://catfact.ninja/fact")
    fact_data = fact_response.json()
    context.response = requests.post(f"{context.base_url}/post-cat-fact", json=fact_data, headers={"Content-Type": "application/json"})

@when('I update a cat fact')
def step_impl(context):
    # Fetch a cat fact first to ensure payload
    fact_response = requests.get("https://catfact.ninja/fact")
    fact_data = fact_response.json()
    context.response = requests.put(f"{context.base_url}/put-cat-fact", json=fact_data, headers={"Content-Type": "application/json"})

@then('I receive a cat fact with status code 200')
def step_impl(context):
    assert context.response.status_code == 200
    assert "fact" in context.response.json()

@then('I receive a success message with status code 200 or 201')
def step_impl(context):
    assert context.response.status_code in [200, 201]
    response_json = context.response.json()
    assert "message" in response_json  # Adjust based on actual expected response



