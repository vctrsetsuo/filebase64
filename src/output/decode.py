import base64

def decode(name):
    with open(name, 'r') as binary_data:
        encoded = binary_data.read()

        input_name = base64.b64decode(name.split('_')[1]).decode("utf-8")

        with open(input_name, "wb") as exe:
            exe.write(base64.b64decode(encoded))