# How to Run This Program:

1) Download the compressed folder and decompress it. After decompressing, make sure that authenticator.py is in the directory.
2) `cd <folder_that_contains_the_file_authenticator.py>`
3) `cd otp`
4) Type in `./setup.sh` in the terminal to set up the libraries for qrcode and Pillow. If this doesn't work, make the file executable by typing in `chmod +x setup.sh` then type in `./setup.sh` again. 
5) Run the program by typing in: `python authenticator.py <parameter>`. Paramater can be either `--generate-qr` or `--get-otp`
6) Follow along the messages in the terminal (or console) window. Enjoy!


## If the Above Method Doesn't Work, Try This Instead:

1) Download the compressed folder and decompress it. After decompressing, make sure that authenticator.py is in the directory.
2) `cd <folder_that_contains_the_file_authenticator.py>`
3) `cd otp`
4) Type in `pip install qrcode`
5) Type in `pip install Pillow`
6) Run the program by typing in: `python authenticator.py <parameter>`. Paramater can be either `--generate-qr` or `--get-otp`