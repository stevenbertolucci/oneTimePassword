# Author: Steven Bertolucci
# Course: CS370 - Introduction to Security
# Assignemnt: Programming Project - OTP
# Due Date: November 17, 2024
# ------------------------------------------------------------
#                           Citations
#
#   I followed along the generateTOTP() function from 
#   RFC 6238 that shows an example implementation on how
#   to generate TOTP. I used the similar code for my 
#   implementation in python for get_otp() function below.
#
# ------------------------------------------------------------

import qrcode
import time
import sys
import hmac
import hashlib

# Initialize secret key
secret = 'JBSWY3DPEHPK3PXP'

# For length of otp
DIGITS_POWER = [1, 10, 100, 1000, 100000, 1000000, 10000000, 100000000]

# Function to generate QR Code
def generate_qr_code():
    # Generate QR code
    uri = f"otpauth://totp/FBI TOP SECRET APP:CS370 - bertolus?secret={secret}&issuer=FBI TOP SECRET APP"

    # Make the QR code
    qr = qrcode.make(uri)

    # Save the QR code
    qr.save("qr_code.jpg")

    print("QR Code saved as \033[93mqr_code.jpg\033[0m \nPlease open the image then open Google Authenticator and scan the qr code.")

# Function to get OTP code
def get_otp():

    # 30 second intervals
    current_time = int(time.time() // 30)

    key = bytearray(b'Hello!\xDE\xAD\xBE\xEF')
    time_bytes = current_time.to_bytes(8, 'big')
    hash = hmac.new(key, time_bytes, hashlib.sha1).digest()

    # Put selected bytes into result int
    offset = hash[-1] & 0x0F
    binary = (
            (hash[offset] & 0x7F) << 24
            | (hash[offset + 1] & 0xFF) << 16
            | (hash[offset + 2] & 0xFF) << 8
            | (hash[offset + 3] & 0xFF)
        )

    otp = binary % DIGITS_POWER[5]

    # If length of the otp is less than 6, fill in the missing digits with 0 on the left side
    return str(otp).zfill(6)


def main():

    # Listen for command --generate-qr
    if '--generate-qr' in sys.argv:
        generate_qr_code()

        # Ask user to verify the code
        user_input = input("\nEnter the code: ")

        current_otp = get_otp()
        # Verify the code
        if user_input == current_otp:
            print("\033[92mAccess granted!\033[0m\n")
        else:
            while(1):
                print("\033[91mStop right there criminal scum! Your otp code is incorrect.\033[0m")

                # Ask user to verify the code
                user_input = input("\nEnter the code: ")

                current_otp = get_otp()

                # Verify the code
                if user_input == current_otp:
                    print("\033[92mAccess granted!\033[0m\n")
                    exit(0)

    # Listen for command --get-otp
    elif '--get-otp' in sys.argv:
        print("\033[34mThis will display the OTP code every 30 seconds. Hit CRTL+C to exit.\033[0m")
        while(1):
            print(get_otp())
            time.sleep(30)

    else:
        print("Missing additional command. Please use \033[93m`python authenticator.py --generate-qr`\033[0m or \033[93m`python authenticator.py --get-otp`\033[0m")
        exit(0)

    exit(0)

if __name__ == "__main__":
    main()