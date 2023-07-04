status_code = 200

if status_code == 200 or status_code == 201:
    print("Success")
elif status_code == 400:
    print("Bad request")
elif status_code == 404:
    print("Not found")
elif status_code == 500 or status_code == 501:
    print("Server error")
else:
    print("Unknown")


# switch statement
match status_code:
    case 200 | 201:
        print("Success")
    case 400:
        print("Bad Request")
    case 404:
        print("Not Found")
    case 500 | 501:
        print("Server error")
    case _:
        print("Unknown")
