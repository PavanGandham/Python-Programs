import io
import segno
from segno import helpers
from urllib.request import urlopen

qrcode = segno.make_qr("Iam Iron Man")

# Create Colorful QR Codes
qrcode.save("qr_code.png",dark='darkred', light='lightblue', border=5, scale=10)

# Dark modules with alpha transparency
qrcode.save("qr_code_2.png",dark='#0000ffcc', scale=10)

# Micro QR Code
micro_qrcode = segno.make('Rain', error='q')
micro_qrcode.save('rain.png',dark='darkblue', data_dark='steelblue', scale=5)

# Save QR Codes in Different Formats
qrcode = segno.make('qr_save')
qrcode.save('qr_save.svg')
qrcode.save('qr_save.png')
qrcode.save('qr_save.eps')

# Make a QR Code for URL Sharing
video = segno.make('https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A')
video.save('video.png', dark="yellow", light="#323524", scale=5)

# Make a QR Code for a WiFi Configuration
wifi_qrcode = helpers.make_wifi(ssid='MyWifi', password='1234567890', security='WPA')
wifi_qrcode.designator
'3-M'
wifi_qrcode.save('wifi-access.png', scale=10)

# Another way to make a QR Code for a wifi configuration
wifi_settings = {
    "ssid": '(Wifi Name)',
    "password": '(Wifi Password)',
    "security": 'WPA',
}
wifi = segno.helpers.make_wifi(**wifi_settings) 

""" If you haven't come across ** in Python before, it's a lovely bit of so-called syntactic sugar that unpacks a dictionary into a series of keyword arguments 
e.g. ssid=”(Wifi Name)”, password=”(Wifi Password)”, security=”WPA”. By creating wifi-settings as a dictionary first and formatting it with one key:value pair per line, 
it's much easier to edit and add to in future, and the function in the following line (wifi= ) is also much more concise and readable as a consequence. """

wifi.save("Wifi.png", dark="yellow", light="#323524", scale=8)

# Encode Contact Details in QR Codes MeCards and Vcards.
contact_qrcode = helpers.make_mecard(name='Pavan Gandham', email='me@example.com', phone='+123456789')
contact_qrcode.designator
'3-L'
# Some params accept multiple values, like email, phone, url
me_card = helpers.make_mecard(name='Pavan Gandham', 
                             email=('me@example.com', 'email@example.com'),
                             url=['http://www.example.com', 'https://example.come/~olu'])
me_card.save('my_contact.png', scale=5)

vcard = segno.helpers.make_vcard(
    name='Pxxx;Jxxx',
    displayname='Times Tables Furniture',
    email=('jxxxpxxx@timestables.furniture'),
    url=[
        'https://www.etsy.com/uk/shop/TimesTablesFurniture',
        'https://www.facebook.com/profile.php?id=100083448533180'
    ],
    phone="+44xxxxxxxxxx",
)
img = vcard.to_pil(scale=6, dark="#FF7D92").rotate(45, expand=True)
img.save('Etsy.png')

# We can add any logo/image as a background to QR Code:
awsom = segno.helpers.make_vcard(
    name='Fison;Pete',
    displayname='AWSOM Solutions Ltd.',
    email=('pxxxfxxx@awsom.solutions'),
    url=[
        'https://twitter.com/awsom_solutions',
        'https://medium.com/@petefison',
        'https://github.com/pfython'
    ],
    phone="+44xxxxxxxxxx",
)

awsom.to_artistic(
    background="logo.png",
    target='AWSOM.png',
    scale=6,
    quiet_zone="#D29500"
)

# QR code, of “Hello World” script written in the Piet programming language:
piet = segno.make('https://esolangs.org/wiki/Piet', error='h')
piet.to_artistic(background="background.png", target='Piet.png', scale=16)

# Keeping everything in memory
"""
-> If you prefer to keep all your processing “in memory” rather than creating files on your hard drive or server, 
you can either create a PIL image object or save a file-like object using BytesIO.
-> Similarly if you prefer to load background images from their URLs directly into memory without 
creating a file on your hard drive or server first, you can use the urlopen method.
"""

beatle = segno.make('Paul McCartney')
beatle = qrcode.to_pil()

buff = io.BytesIO()
beatle.save(buff, kind='svg')

red_beatle = segno.make('Ringo Starr', error='h')
url = 'https://media.giphy.com/media/HNo1tVKdFaoco/giphy.gif'
bg_file = urlopen(url)
red_beatle.to_artistic(background=bg_file, target='ringo.gif', scale=10)

# Article Sources : 
"""
-> https://www.freecodecamp.org/news/how-to-create-stunning-qr-codes-with-python/
-> https://medium.com/pythoniq/make-beautiful-qr-codes-in-python-ef083fb38550 
"""

# Requirements: 
"""
    1. pip install segno
    2. pip install qrcode-artistic
    
"""
