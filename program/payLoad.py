def create_book_payload(isbn, aisle):
    payload = {
        "name": "Learn Appium Automation with Java",
        "isbn": isbn,
        "aisle": aisle,
        "author": "John Doe"
    }
    return payload


def build_payload_from_db(query_result):
    if len(query_result) < 4:
        raise ValueError("Query result should contain at least 4 elements (name, isbn, aisle, author).")

    payload = {
        "name": query_result[0],
        "isbn": query_result[1],
        "aisle": query_result[2],
        "author": query_result[3]
    }
    return payload