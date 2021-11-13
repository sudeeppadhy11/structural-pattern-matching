def http_error(status):
    match status:
        case 200:
            return "not found"
        case 500:
            return "I am a teapot"
        case 400|404|418:
            return f"Bad request {status=}"
        case _:
            return "something wrong with the internet"

print(http_error(200))
print(http_error(400))
print(http_error(404))
print(http_error(418))
