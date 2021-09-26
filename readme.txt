1. Author: Edward Nardo, JHED ID: C2FFF9
2. Module Info: Module 8/9, Frequency Analysis, due: Sunday, April 04, 2021
3. Approach:
ifsr.py - I began by creating my class and stubbing out all of its methods.  I started with the constructor which takes
a seed and a tap.  I set the self values to the parameters passed in.  The length method just returns the length of
self.seed.  The bit method takes an int as a parameter and returns the index of self.seed at the parameter passed in.
The step method does an xor with the first bit and the tap bit.  It then concats the new bit onto the end of the seed
while shedding the first leftmost bit of the seed(as a string).  The assignment outline says to return the rightmost bit, but I
decided to return the seed as an integer value instead.  I did this to simplify the program in image_encryptor.py.  The
__str__ method returns the seed to be printed as a string when called.  I then check if __name__ == main and if it does
I print the 5 lfsr values for the assignment.

image_encrypter.py - I began by creating my class and stubbing out all of its methods.  I started with the constructor which takes
an instance of an LFSR class, a filename, and a boolean value called decrypt(I added this).  I set the self values to the parameters
passed in.  The open_image method takes a parameter filename as a string and opens the image associated with the
filename.  If the boolean parameter decrypt is true I then rotate and mirror the image.  I had an issue where my football
was getting mirrored and looked almost identical, but it was upside down, so my decypted image was wrong.  So for this
reason I had to mirror the image.  I then return the image.  The pixel_array method calls the open_image method
and saves it to a variable.  I then call Image.load() which loads the pixels of the image into a list.  I then get the
dimensions of the image.  I then loop through the pixels and save them to a new nested list so they can be manipulated
easier.  I then return the new list.  The transform method takes that new list and loops through each tuple of RGB values.
For each tuple, it xor's the current r,g,or b value with a new lfsr step value and saves to a new tuple(since tuples are
immutable).  I then save the tuples to a new list and the lists to an outter list forming the original 2d list.  I then
return this new list.  The save_image method saves an image but is currently unused.  I then check if __name__ == main and if it does
I create an instance of lfsr.  I then create an instance of imageEncrypter passing in the instance of lfsr, along with
the image and a boolean.  I then call the transform method.  I then flatten the 2d array returned because image.save takes
a 1d array.  I then create a new image using Image.new and put the rgb values in it using Image.put.  I then save the image
as football_encrytped.png.  I then create a new lfsr with the same initial seed.  I create a new instance of imageEncrypter
and pass in the new lfsr instance, the football_encrypted.png image name, and true for the bool value.  Everything after
this is the same as before in the main method.



4. Known bugs:  None that I know of