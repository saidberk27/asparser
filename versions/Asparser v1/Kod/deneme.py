import qrcode as qrcode


if __name__ == '__main__':
    qrMetinTemel = 'Safeline ASP-EI{} {} {} {} https://www.asparenerji.com'
    eldivenType = "S"
    sinifInput = "CLASS 00"
    i = "38948392"
    uretimTarih = "12/21"


    input_data = qrMetinTemel.format(eldivenType, sinifInput, i, uretimTarih)


    qr = qrcode.QRCode(version=1, box_size=10, border=5)


    qr.add_data(input_data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save('qrcode001.png')

