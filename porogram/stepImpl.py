import requests
from behave import *
from payLoad import *
from properties import *
from resources import *


@given('the Book details which needs to be added to Library')
def step_impl(context):
    context.urla = endpointUrl + ApiResources.addBook
    context.headers = {"Content-Type": "application/json"}
    context.payLoad = addBookPayload("dbdb")

@when('we execute the AddBook PostAPI method')
def step_impl(context):
    context.addBook_response = requests.post(urla, json=addBookPayload("fsfsf",1234), headers=headers,)


@then('book is successfully added')
def step_impl(context):
    print(response_json["Msg"])
    context.bookId = response_json['ID']
    assert response_json["Msg"] == "successfully added"





