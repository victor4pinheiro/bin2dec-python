"""
Convert binary to decimal number
"""


def convert_binary_to_decimal(binary_number: str):
    """Convert the already authenticated binary number to decimal number"""
    count = len(binary_number)
    result = 0

    for bit in binary_number:
        result += int(bit) * pow(2, count - 1)
        count -= 1
    print(result)


def handle_error(message: str):
    """Print error on screen"""
    print(message)


def check_binary(value: str) -> bool:
    """Check if value is a binary number"""
    state_bits = '01'
    count = 0
    for bit in value:
        if bit not in state_bits:
            count = 1
            break

    if count:
        status = False
        handle_error('It is not a binary number.')
    else:
        status = True

    return status


def check_integer(value: str) -> bool:
    """Check if value is only number"""
    if value.isdecimal():
        status_check_binary = check_binary(value)
    else:
        status_check_binary = False
        handle_error('Error! Value does not contain only number')

    return status_check_binary


def check_length(value: str) -> bool:
    """Check if value is a byte"""
    if len(value) <= 8:
        status_check_integer = check_integer(value)
    else:
        status_check_integer = False
        handle_error("Error! It is not a byte")

    return status_check_integer


print('Hello. To convert a binary number, please enter a valid value:')
INPUT_USER = input()

STATUS_VALIDATE = check_length(INPUT_USER)

if STATUS_VALIDATE is True:
    convert_binary_to_decimal(INPUT_USER)
