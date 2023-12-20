from django.http import HttpResponse
from django.shortcuts import render
from qrcode import *
# data = None
import os
from django.http import HttpResponseRedirect
from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import webbrowser
import segno
import io
from PIL import Image
from segno import helpers
from qrcode_artistic import write_artistic


def home(request):
    
    if request.method == 'POST':
        print("1")
        data = request.POST['data']
        # img.save('qrgen/static/image/test.png')
        color = request.POST.get('color')
        s_video= segno.make(data)
        s_video.save("qrgen/static/image/funny001.png" ,scale=5,dark=color)
        print(2)
        message = "Qr Created successfully"
        return render(request, 'home.html', {'data': data, 'message': message})
    else:
        return render(request, 'home.html', {})
    
def scan(request):
    return render(request, 'qrreader.html')

def Normal_page(request):
    return render(request, 'normal.html')
 
    
    
def wifi_gen(request):
    
    if request.method == 'POST':
        print("1")
        # data = request.POST['data']
        # s_video= segno.make("https://tenor.com/view/chutiya-banaya-tumko-mirzapur-gif-21771920")
        # s_video.save("qrgen/static/funny001.png" ,scale=5,dark='#16a085')
        ssid = request.POST.get('ssid')
        password = request.POST.get('password')
        security = request.POST.get('security')
        color = request.POST.get('color')
        # print("ccc", ssid ,password ,security)
        wifi_setting ={
           'ssid': ssid,
          'password': password,
          'security': security
          }
        print("hifi settings:",wifi_setting)
        wifi = helpers.make_wifi(**wifi_setting)
        wifi.save("qrgen/static/image/wifi1.png",dark=color,scale=6)
        # print(2)
        message = "Qr Created successfully"
        return render(request, 'wifi.html', { 'password': password,'ssid':ssid,'security':security, 'message': message})
    else:
        return render(request, 'wifi.html', {})


def contact_me(request):
    
    if request.method == 'POST':
        print("1")
        # data = request.POST['data']
        # s_video= segno.make("https://tenor.com/view/chutiya-banaya-tumko-mirzapur-gif-21771920")
        # s_video.save("qrgen/static/funny001.png" ,scale=5,dark='#16a085')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        url = request.POST.get('url')
        country = request.POST.get('country')
        color = request.POST.get('color')
        print("ccc", name ,email ,phone, url,country)
        qrcode_me = helpers.make_mecard(
        name=name,
        email= email,
        phone= phone,
        url=url,
        country=country
        )

        qrcode_me.save("qrgen/static/image/contact_me.png",scale=6,dark=color)
        # print(2)
        message = "Qr Created successfully"
        return render(request, 'contactme.html', { 'name': name,'email':email,'phone':phone, 'message': message})
    else:
        return render(request, 'contactme.html', {})
    

def resume_qr(request):
    
    if request.method == 'POST':
        print("1")
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        background = request.FILES.get('image')
        url = request.POST.get('url')
        country = request.POST.get('country')
        city = request.POST.get('city')
        title = request.POST.get('title')
        color = request.POST.get('color')
        qrcode_v = helpers.make_vcard(
             name=name,
             photo_uri =  background,
             displayname=name,
             email= email,
             phone= phone,
             url=url,
             country=country,
             city=city,
             title=title
    
         )

        qrcode_v.save("qrgen/static/image/contact_me_profile.png",scale=6,dark=color)
        
        # print(2)
        message = "Qr Created successfully"
        return render(request, 'resumeqr.html', { 'name': name,'email':email,'phone':phone, 'message': message})
    else:
        return render(request, 'resumeqr.html', {})
    
    

def image_bg(request):
    
    if request.method == 'POST':
        print("1")
        background = request.FILES.get('image')
        print(background)
        # qrcode_img = segno.make("qrcode with Image", error='h')
        qrim =  request.POST.get('url')
        print(qrim)
        qrcode_img = segno.make(qrim, error='h')
        write_artistic(qrcode_img, background=background,target='qrgen/static/image/qr_neww.png', scale=5)

        # qrcode_me.save("qrgen/static/image/contact_me.png",scale=6,dark=color)
        # print(2)
        message = "Qr Created successfully"
        return render(request, 'bgimage.html', { 'background':background,'url':qrcode_img,'message': message})
    else:
        return render(request, 'bgimage.html', {})
    
    

def logo_maker(request):
    
    if request.method == 'POST':
        print("1")
        logo = request.FILES.get('image')
        print(logo)
        # qrcode_img = segno.make("qrcode with Image", error='h')
        qrim =  request.POST.get('url')
        print(qrim)
        qrcode_img = segno.make(qrim, error='h')
        # write_artistic(qrcode_img, background=background,target='qrgen/static/image/qr_neww.png', scale=5)


        qr_logo = segno.make(qrim,error='h')
        qr_logo.save('qrgen/static/image/qr_logo.png',scale=6)

        img= Image.open('qrgen/static/image/qr_logo.png')
        img = img.convert('RGB')

        img_width , img_height = img.size

        logo_img = Image.open(logo)

        logo_max_size = img_height // 3

        logo_img.thumbnail((logo_max_size,logo_max_size),Image.LANCZOS)
        box = ((img_width - logo_img.size[0])//2  ,(img_height - logo_img.size[1] ) //2  )
        img.paste(logo_img,box)
        img.save('qrgen/static/image/Qrcode_with_logo.png')
        message = "Qr Created successfully"
        return render(request, 'logomaker.html', { 'logo':logo,'url':qrcode_img,'message': message})
    else:
        return render(request, 'logomaker.html', {})
    















# def scan(request):
#     return render(request, 'qrreader.html')
    
    
    
 # def home(request):
#     global data
#     if request.method == 'POST':
#         data = request.POST['data']
#         img = make(data)
#         img.save('/qrgen/static/test.png')
#     else:
#         pass
#     return render(request,'home.html',{'data':data})   
    
    
# def qr_scanner(request):
#     cap = cv2.VideoCapture(0)
#     detector = cv2.QRCodeDetector()

#     while True:
#         _, img = cap.read()
#         data, _, _ = detector.detectAndDecode(img)

#         if data:
#             a = data
#             break

#         cv2.imshow('QR Code Scanner', img)

#         if cv2.waitKey(1) == ord('q'):
#             break

#     b = webbrowser.open(str(a))
#     cap.release()
#     cv2.destroyAllWindows()

#     return render(request, 'qrreader.html', {'qr_content': a})



# @csrf_exempt
# def process_webcam_stream(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         webcam_image = data['image']

#         # Decode QR code from the webcam image
#         qr_code_data = decode_qr_code(webcam_image)

#         # Return the QR code data or an error message
#         if qr_code_data:
#             return JsonResponse({'qr_code_data': qr_code_data})
#         else:
#             return JsonResponse({'error': 'QR code not found'})

#     return JsonResponse({'error': 'Invalid request'})



def handler404(request,exception=None):
   return render(request,'404.html',{})

def custom404(request,exception=None):
   return JsonResponse({
      'status_code':404,
      'error':'The resource was not found'
   })
handler404 = handler404