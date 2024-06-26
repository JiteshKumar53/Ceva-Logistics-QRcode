import qrcode
from pyzbar.pyzbar import decode 
from PIL import Image

myqr= qrcode.make("https://www.cevalogistics.com/en/careers/teams/e-commerce/sweden")
myqr1= qrcode.make(" https://www.google.com/maps/place/CEVA+Logistics/@59.5103322,17.722328,17z/data=!3m1!4b1!4m6!3m5!1s0x465fa388960b5457:0x7f74f959eaac95e1!8m2!3d59.5103322!4d17.7249029!16s%2Fg%2F11fkn0w6jk?entry=ttu")


myqr.save("Website.png",scale= 8)
myqr1.save("Address.png",scale= 8)



b= decode(Image.open("myqr.jpg"))
print(b[0].data.decode("ascii"))