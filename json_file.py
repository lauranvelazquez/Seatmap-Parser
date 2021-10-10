import json
import os
from seat_reg import *


# Convert data to json
def json_generate(seats, file_name):
    file_name = file_name + '_parsed.json'
    with open(os.path.join(file_name), 'w') as file:
        for s in seats:
            data = {}
            data['Seat Number'] = s.seatNumber
            data['Row'] = s.rowNumber
            data['Plane Section'] = s.planeSection
            data['Available'] = s.available
            data['Features'] = s.features
            data['Extensions'] = s.extension
            data['Code Context'] = s.codeContext
            data['Price'] = s.price
            data['Currency Code'] = s.currencyCode
            js = {}
            js['Seat:'] = data
            json.dump(js, file, indent=4)

    return file_name
