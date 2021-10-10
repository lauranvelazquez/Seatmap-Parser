from xml.etree.ElementTree import parse
from seat_reg import *


# Read xml and search data
def read_xml(file_name):
    xml_data = []
    document = parse(file_name)
    root = document.getroot()

    #Seatmap1
    if file_name == 'seatmap1.xml':
        seatsData = root.iter('{http://www.opentravel.org/OTA/2003/05/common/}RowInfo')

        for row in seatsData:

            rowNumber = row.get('RowNumber')

            for seat in row:
                planeSection = seat.get('PlaneSection')

                for info in seat:
                    seatNumber = info.get('SeatNumber')

                    if seatNumber != None:
                        availableInd = info.get('AvailableInd')
                        features_list = []
                        extension_list = []

                        features = seat.findall('{http://www.opentravel.org/OTA/2003/05/common/}Features')
                        for f in features:
                            features_list.append(f.text)
                            extension_list.append(f.get('extension'))

                        try:
                            service = seat.find('{http://www.opentravel.org/OTA/2003/05/common/}Service')
                            codeContext = service.get('CodeContext')
                        except:
                            codeContext = None

                        try:
                            fee = service.find('{http://www.opentravel.org/OTA/2003/05/common/}Fee')
                            price = fee.get('Amount')
                            currencyCode = fee.get('CurrencyCode')
                        except:
                            price = None
                            currencyCode = None

                        seat_list = Seat(rowNumber, planeSection, availableInd, seatNumber, features_list, extension_list,
                                         codeContext, price, currencyCode)
                        xml_data.append(seat_list)

    #Seatmap2
    else:
        seatsData = root.findall('{http://www.iata.org/IATA/EDIST/2017.2}SeatMap')

        for seatInfo in seatsData:
            cabin = seatInfo.find('{http://www.iata.org/IATA/EDIST/2017.2}Cabin')
            row = cabin.find('{http://www.iata.org/IATA/EDIST/2017.2}Row')
            number = row.find('{http://www.iata.org/IATA/EDIST/2017.2}Number')
            rowNumber = number.text

            seat = row.find('{http://www.iata.org/IATA/EDIST/2017.2}Seat')
            seats = seat.findall('{http://www.iata.org/IATA/EDIST/2017.2}SeatDefinitionRef')

            for s in seats:
                features_list = []
                extension_list = []
                seatNumber = s.text

                column = seat.find('{http://www.iata.org/IATA/EDIST/2017.2}Column')
                planeSection = column.text

                if planeSection == 'A' or planeSection == 'F':
                    features_list.append('Window')
                elif planeSection == 'C' or planeSection == 'D':
                    features_list.append('Aisle')
                else:
                    features_list.append('None')

                try:
                    ext = seat.find('{http://www.iata.org/IATA/EDIST/2017.2}OfferItemRefs')
                    extension = ext.text
                    extension_list.append(extension)
                except:
                    extension_list.append('None')

                if extension == 'OFIa20ae42f-6417-11eb-b326-15132ca0c3351':
                    price = 22.10
                elif extension == 'OFIa20ae42f-6417-11eb-b326-15132ca0c3352':
                    price = 35.40
                elif extension == 'OFIa20ae42f-6417-11eb-b326-15132ca0c3353':
                    price = 17.70
                elif extension == 'OFIa20ae42f-6417-11eb-b326-15132ca0c3354':
                    price = 11.50
                else:
                    price = None

                availableInd = True
                currencyCode = 'GPB'
                codeContext = None

                seat_list = Seat(rowNumber, planeSection, availableInd, seatNumber, features_list, extension_list,
                                 codeContext, price, currencyCode)
                xml_data.append(seat_list)

    return xml_data