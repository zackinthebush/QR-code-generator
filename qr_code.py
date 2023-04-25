import qrcode
from PIL import Image

def generate_qr_code(url, logo_path, qr_color='green', qr_size=100):
    # Load logo image and resize it
    logo = Image.open(logo_path)
    basewidth = qr_size
    wpercent = (basewidth / float(logo.size[0]))
    hsize = int((float(logo.size[1]) * float(wpercent)))
    logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)

    # Generate QR code
    qr_code = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr_code.add_data(url)
    qr_code.make()
    
    # Generate QR code image with logo
    qr_img = qr_code.make_image(fill_color=qr_color, back_color="white").convert('RGB')
    pos = ((qr_img.size[0] - logo.size[0]) // 2, (qr_img.size[1] - logo.size[1]) // 2)
    qr_img.paste(logo, pos)

    # Save the QR code image
    qr_img.save('gfg_QR.png')
    print('QR code generated!')

# Example usage
url = 'https://gdsc.community.dev/university-of-batna-2/'
logo_path = 'C:/Users/zack/Desktop/gdsc-logo.png'
generate_qr_code(url, logo_path, qr_color='green', qr_size=100)
