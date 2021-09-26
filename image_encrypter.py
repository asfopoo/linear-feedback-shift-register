from lfsr import LFSR
from PIL import Image, ImageOps


class ImageEncrypter:
    # constructor
    def __init__(self, lfsr: LFSR, file_name: str, decrypt):
        self.lfsr = lfsr
        self.file_name = file_name
        self.decrypt = decrypt

    # open the image specified by ‘file_name’
    # you will find the Image.open method useful here
    def open_image(self, file_name: str):
        # open an image using pil library
        im = Image.open(file_name)
        # if decrypting the image is rotated and mirrored so fix it and return if not just return the image as is
        if self.decrypt:
            im = im.rotate(270)
            im_mirror = ImageOps.mirror(im)
            return im_mirror
        # return the image
        return im

    # convert the image to a 2D array of tuples of the form (R, G, B)
    # read in from open_image() and return the 2D array
    # you will find the Image.load method useful here
    def pixel_array(self):
        # open the image by calling the open_image method
        im = self.open_image(self.file_name)
        # load the image getting back list of pixels
        px = im.load()
        # get sizes of image and save to width and height
        width, height = im.size

        # print(px[0, 0])

        # create a new list to add new pixel values to
        all_pixels = []
        # loop rows of image
        for x in range(width):
            # add a nested set of lists for every row that will get added to all_pixels
            row_of_pixels = []
            # loop pixels
            for y in range(height):
                # save the current pixel - a tuple of 3 rgb values
                pixel = px[x, y]
                # append the pixels to the current row
                row_of_pixels.append(pixel)
            # finished the outter loop, append the row of pixels to the list of all pixels
            all_pixels.append(row_of_pixels)
        # return the new list
        return all_pixels

    # encrypts the 2D array returned from pixel_array(),
    # returns the encrypted 2D array
    # you will find the binary XOR operator useful here
    def transform(self):
        # get the new pixel array
        pixel_array = self.pixel_array()
        encrypt_array = []
        # loop the pixel array and create a new list of lists similar to the pixel array method
        for x in pixel_array:
            transformed_rows = []
            for y in x:
                # append the tuple of each rgb value xor'd with a new step value
                transformed_rows.append((y[0] ^ self.lfsr.step(),
                                         y[1] ^ self.lfsr.step(),
                                         y[2] ^ self.lfsr.step()))
            # append the row to the encrypt_array list
            encrypt_array.append(transformed_rows)
        # return the encrypted list of values
        return encrypt_array

    # converts the encrypted 2D array back into an image named ‘file_name’
    # you will find the Image.save method useful here
    def save_image(self, file_name: str):
        Image.save(file_name)


# your executable code that invokes ImageEncrypter and encrypts/decrypts an
# image and saves the result to a file
if __name__ == "__main__":
    # create an instance of LFSR called seed_1
    seed_1 = LFSR('10011010', 5)
    # create an instance of ImageEncrypter
    image_encryptor = ImageEncrypter(seed_1, 'football.png', False)
    # call the transform method
    encrypted_pixels = ImageEncrypter.transform(image_encryptor)
    # create a new list of pixels to save
    encrypted_pixels_to_save = []
    # loop through the encrypted pixels and flatten them - image.save takes a single list
    for row in encrypted_pixels:
        for tup in row:
            encrypted_pixels_to_save.append(tup)
    # create a new image
    encrypted_image = Image.new('RGB', (225, 225))
    # put the pixels in the new image
    encrypted_image.putdata(encrypted_pixels_to_save)
    # save the image
    encrypted_image.save('football_encrypted.png')

    # create a seed object
    seed_2 = LFSR('10011010', 5)
    # create an instance of ImageEncrypter to decrypt
    image_decrypter = ImageEncrypter(seed_2, 'football_encrypted.png', True)
    # call the transform method
    decrypted_pixels = ImageEncrypter.transform(image_decrypter)
    # create a new list of pixels to save
    decrypted_pixels_to_save = []
    # loop through the decrypted pixels and flatten them - image.save takes a single list
    for rows in decrypted_pixels:
        for tuples in rows:
            decrypted_pixels_to_save.append(tuples)
    # create a new image
    decrypted_image = Image.new('RGB', (225, 225))
    # put the pixels in the new image
    decrypted_image.putdata(decrypted_pixels_to_save)
    # the image is rotated and mirrored so fix it
    decrypted_image = decrypted_image.rotate(270)
    decrypted_image = ImageOps.mirror(decrypted_image)
    # save the image
    decrypted_image.save('football_decrypted.png')
