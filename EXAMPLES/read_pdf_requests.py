#!/usr/bin/env python

import sys
import os

import requests
import magic

# url = 'https://www.nasa.gov/pdf/739318main_ISS%20Utilization%20Brochure%202012%20Screenres%203-8-13.pdf'  # <1>
url = 'https://www.bnymellon.com/content/dam/bnymellon/documents/pdf/aerial-view/why-outsourcing-is-turning-trading-inside-out.pdf.coredownload.pdf'
#saved_pdf_file = 'nasa_iss.pdf'  # <2>
saved_pdf_file = 'bnym.pdf'

response = requests.get(url)  # <3>
if response.status_code == requests.codes.OK:  # <4>
    data_type = magic.from_buffer(response.content)
    print("DATA TYPE:", data_type)
    if response.headers.get('content-type') == 'application/pdf':
        with open(saved_pdf_file, 'wb') as pdf_in:  # <5>
            pdf_in.write(response.content)  # <6>

        if sys.platform == 'win32':  # <7>
            cmd = saved_pdf_file
        elif sys.platform == 'darwin':
            cmd = 'open ' + saved_pdf_file
        else:  # Linux,etc
            cmd = 'acroread ' + saved_pdf_file

        os.system(cmd)  # <8>
