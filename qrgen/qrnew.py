import segno
import io
from PIL import Image
from segno import helpers
from qrcode_artistic import write_artistic

# s_video= segno.make("https://tenor.com/view/chutiya-banaya-tumko-mirzapur-gif-21771920")
# s_video.save("funny001.png" ,scale=5,dark='#16a085')
# Apply a linear gradient with blue and grey to the QR code


# Image.open("google.png")

# wifi_setting ={
#     'ssid': 'JioFiber-6p20i',
#     'password': '987654321',
#     'security': 'WPA2-Personal'
# }
# wifi_setting ={
#     'ssid': 'JioFiber-6p20i',
#     'password': '987654321',
#     'security': 'WPA'
# }

# This is for wifi

# wifi_setting ={
#     'ssid': 'realme 6',
#     'password': 'utkarsh hg',
#     'security': 'WPA'
# }

# wifi = helpers.make_wifi(**wifi_setting)
# wifi.save("wifi1.png",dark='blue',scale=6)


# Personalized Cards to save contacts
# qrcode_me = helpers.make_mecard(
#     name="Utkarsh Gupta",
#     email= 'utkarshhg911@gmail.com',
#     phone='+917987674357',
#     url='https://github.com/Shadowsweep',
#     country='India'
# )

# qrcode_me.save("contact_me.png",scale=6,dark='#30e14e')

#make_vcard


# Personalized Cards to save contacts
# qrcode_v = helpers.make_vcard(
#     name="Utkarsh Gupta",
#     displayname="Utkarsh Gupta",
#     email= 'utkarshhg911@gmail.com',
#     phone='+917987674357',
#     url='https://github.com/Shadowsweep',
#     country='India',
#     city='gwalior',
#     title='Django Developer'
    
# )

# qrcode_v.save("contact_me_profile.png",scale=6,dark='#30e14e')


# coloured bg image
# qrcode_img = segno.make("qrcode with Image", error='h')
# write_artistic(qrcode_img, background="logo1.png",target='qr_neww.png', scale=5)

# Qr code Gif
# qrcode_gif = segno.make("qr code with gif" , error ='h')
# write_artistic(qrcode_gif,background='minions1.gif',target='qr_minions.gif',scale=6)


# Qr logo

# qr_logo = segno.make("https://www.youtube.com/@techunsatisfied",error='h')
# qr_logo.save('qr_logo.png',scale=6)

# img= Image.open('qr_logo.png')
# img = img.convert('RGB')

# img_width , img_height = img.size

# logo_img = Image.open('logo1.png')

# logo_max_size = img_height // 3

# logo_img.thumbnail((logo_max_size,logo_max_size),Image.LANCZOS)
# box = ((img_width - logo_img.size[0])//2  ,(img_height - logo_img.size[1] ) //2  )
# img.paste(logo_img,box)
# img.save('Qrcode_with_logo.png')
