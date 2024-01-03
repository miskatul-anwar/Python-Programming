#! python
import qrcode
import os
code = input("Link: ")
img = qrcode.make(code)
img.save("Qr_code.png","PNG")
os.system("open Qr_code.png")
