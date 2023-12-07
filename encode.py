import base64

with open("file.exe", 'rb') as binary_file:
    binary_data = binary_file.read()
    encoded_data = base64.b64encode(binary_data)

    with open("output", "wb") as output:
        output.write(encoded_data)