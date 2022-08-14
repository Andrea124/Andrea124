import json

""" Calculate fibonacci serie with the limit parameter and save the parameter in file_fibonacci.json"""
def calculate_fibonacci(item_end):
    if upload_valid_numbers(item_end, True):
        numbers_fibonacci = []
        number_one = 0
        number_two = 1
        if item_end < 1:
            return 0
        else:
            for item in range(item_end):
                sum = number_one + number_two
                numbers_fibonacci.append(sum)
                number_one = number_two
                number_two = sum
        return numbers_fibonacci
    else:
        return {"message": "Error with file_numbers.json"}


""" Obtain all the values of file_fibonaccin.json"""
def get_valid_numbers():
    try:
        with open('utils/file_numbers.json') as f:
            payload = json.load(f)
            f.close()
        return payload
    except Exception:
        return {"message": "Error with file_numbers.json"}


""" Add and delete value on file_fibonacci.json"""
def upload_valid_numbers(item_end, action):
    try:
        with open('utils/file_numbers.json', 'r+') as f:
            payload = json.load(f)
            if action:
                if item_end not in payload['valid_numbers']:
                    payload['valid_numbers'].append(item_end)
            else:
                if item_end in payload['valid_numbers']:
                    payload['valid_numbers'].remove(item_end)
                else:
                    return "The number is invalid"
            f.seek(0)
            json.dump(payload, f, indent=4)
            f.truncate()
            f.close()
            return "Action success"
    except Exception:
        return False
