import os
import base64

def encode(name):

    output_name = "output_" + base64.b64encode(name.encode()).decode("utf-8")

    with open(name, 'rb') as binary_file:
        binary_data = binary_file.read()
        encoded_data = base64.b64encode(binary_data)

        with open(output_name, "wb") as output:
            output.write(encoded_data)
    
    return output_name