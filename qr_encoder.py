import qrcode
import cv2                     # For image processing
from pyzbar.pyzbar import decode

# Function to encrypt the data into a QR code 
def encrypt_data(data, filename):
    # Create the QR code object
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    # Add the data to link to the QR code
    qr.add_data(data)
    # Make the QR code adjust to the size of the data
    qr.make(fit=True)
    # Image representation of the QR code
    img = qr.make_image(fill='black', back_color='white')
    # Save the image to a file
    img.save(filename)

#function to decrypt the data
def decrypt_data(filename):
    # Read the image using OpenCV
    img = cv2.imread(filename)
    
    # Decode the QR code
    decoded_objects = decode(img)
    
    # Print the decoded data
    for obj in decoded_objects:
        print(f'Decoded Data: {obj.data.decode("utf-8")}')



# Execution example 
if __name__ == "__main__":  # Corrected this line
    data = "hey there "
    filename = "image.png"
    encrypt_data(data, filename)
    decrypt_data(filename)
    print(f"QR code was made successfully in {filename}")
