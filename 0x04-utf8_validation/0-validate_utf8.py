#!/usr/bin/python3
'''module to validate UTF8 data'''


def validUTF8(data):
    '''check for validity of data in UTF8'''

    # Helper function to check if a given byte is a valid UTF-8 start byte
    def is_start_byte(byte):
        '''Helper function to check if a given
        byte is a valid UTF-8 start byte'''
        return ((byte & 0b10000000) == 0b00000000
                or (byte & 0b11100000) == 0b11000000
                or (byte & 0b11110000) == 0b11100000
                or (byte & 0b11111000) == 0b11110000)

    # Helper function to get the number of
    # continuation bytes based on the start byte
    def get_num_cont_bytes(start_byte):
        '''Helper function to get the number
        of continuation bytes based on the start byte'''
        if (start_byte & 0b11100000) == 0b11000000:
            return 1
        elif (start_byte & 0b11110000) == 0b11100000:
            return 2
        elif (start_byte & 0b11111000) == 0b11110000:
            return 3
        return 0

    index = 0
    while index < len(data):
        start_byte = data[index]
        num_cont_bytes = get_num_cont_bytes(start_byte)

        # Check if the start byte is a valid UTF-8 start byte
        if (not is_start_byte(start_byte)
                or num_cont_bytes + index + 1 > len(data)):
            return False

        # Check continuation bytes
        for i in range(index + 1, index + num_cont_bytes + 1):
            if (data[i] & 0b11000000) != 0b10000000:
                return False

        index += num_cont_bytes + 1

    return True
