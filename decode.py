import base64

with open('outputjoin', 'r') as binary_data:
    encoded = binary_data.read()

    with open("output.exe", "wb") as exe:
        exe.write(base64.b64decode(encoded))