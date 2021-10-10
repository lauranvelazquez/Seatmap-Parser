# Seatmap-Parser

This program aims to read the transaction data in xml format, identify the important data and return it in json format.
To run the program you must enter the address of the program folder in the console and then enter: python seatmap_parser.py [FILENAME].
The output of the program is a file with this format: FILENAME_parsed.json

# Moduls

• seat_reg: class 'Seat'.
• seatmap_parser: Main script.
• json_file: It receives a list of records and translates them to json format. Returns a .json file.
• xml_file: It receives an .xml file and returns a list of records.

#Files

• seatmap1.xml, seatmap2.xml (input)
• seatmap1_parsed.json, seatmap2_parsed.json (output)