import qrcode
import random
def main():
    name = input(str('Nombre de tu QR: \n'))
    url = input(str('Introduce la url para genera el Codigo QR: \n'))

    qr_codeGenerator(url, name)

    # https://footballexpressferbaeza.herokuapp.com/
    # https://ferbaeza-portfolio.herokuapp.com/

def qr_codeGenerator(url, name):
    imgnumber = random.randrange(1,2**64)
    qr = qrcode.QRCode(
        version=1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size =10,
        border=1
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color='#008080', back_color='#fff')
    img.save("QR_"+name +"__"+ str(imgnumber)+".png")
    #img.save("QR_"+ name +".png")
    


if __name__=='__main__':
    main()