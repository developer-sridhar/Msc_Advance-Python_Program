import numpy as np
from PIL import Image as im

def main():
    # Create an array of shape (1024, 720) with values ranging from 0 to 737279
    array = np.arange(0, 737280, 1, dtype=np.uint8)
    print(type(array))
    print(array.shape)
    
    # Reshape the array to (1024, 720)
    array = np.reshape(array, (1024, 720))
    print(array.shape)
    print(array)

    # Create an image from the array and save it
    data = im.fromarray(array)
    data.save('gfg_dummy_pic.png')

if __name__ == "__main__":
    main()


# OUTPUT
# <class 'numpy.ndarray'>
# (737280,)
# (1024, 720)
# [[  0   1   2 ... 205 206 207]
#  [208 209 210 ... 157 158 159]
#  [160 161 162 ... 109 110 111]
#  ...
#  [144 145 146 ...  93  94  95]
#  [ 96  97  98 ...  45  46  47]
#  [ 48  49  50 ... 253 254 255]]