import requests
from payLoad import *
from program.config.properties import *
from program.config.resources import *

def perform_book_operations(title, price):
    headers = {"Content-Type": "application/json"}
    urla = endpointUrl + ApiResources.addBook
    urlb = endpointUrl + ApiResources.deleteBook

    addBook_response = requests.post(urla, json=addBookPayload(title, price), headers=headers)
    response_json = addBook_response.json()

    print(response_json["Msg"])
    bookId = response_json['ID']
    assert response_json["Msg"] == "successfully added"

    response_deleteBook = requests.post(urlb, json={"ID": bookId}, headers=headers)

    assert response_deleteBook.status_code == 200
    res_json = response_deleteBook.json()

    print(res_json["msg"])
    assert res_json["msg"] == "book is successfully deleted"


if __name__ == "__main__":
    perform_book_operations("fsfsf", 1234)
