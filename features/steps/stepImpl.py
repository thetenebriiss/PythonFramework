import requests
from behave import *
from program.payLoad import *
from program.config.properties import *
from program.config.resources import *



# Given step
@given('the Book details which needs to be added to Library')
def step_given(context):
    context.urla = endpointUrl + ApiResources.addBook
    context.headers = {"Content-Type": "application/json"}
    context.payLoad = create_book_payload("dbdb", 1124)

# When step
@when('we execute the AddBook PostAPI method')
def step_when(context):
    context.addBook_response = requests.post(context.urla, json=context.payLoad, headers=context.headers)

# Then step
@then('book is successfully added')
def step_then(context):
    context.response_json = context.addBook_response.json()
    print(context.response_json["Msg"])
    context.bookId = context.response_json['ID']
    assert context.response_json["Msg"] == "successfully added"



@given('the Book details with {isbn} and {aisle}')
def step_impl(context,isbn,aisle):
    context.urla = endpointUrl + ApiResources.addBook
    context.headers = {"Content-Type": "application/json"}
    context.payLoad = create_book_payload(isbn, aisle)

@then('status code of response should be 200')
def step_impl(context):
    assert context.addBook_response.status_code == 200



