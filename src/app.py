import qrcode
import time

def run():
    modal = """
    What data do you want to encode in QR?

    Enter the data: """

    data = input(modal)

    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image()

    current_time = int(time.time())
    timeStamp = time.strftime('%d-%m-%Y_%H-%M-%S', time.localtime(current_time))

    img.save(f'./src/qr-codes/{timeStamp}.png')



if __name__ == "__main__":
    run()