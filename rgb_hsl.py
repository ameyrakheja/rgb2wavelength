# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 11:02:34 2021

"""
# codedrome.com - RGB to HSL Conversion

import sys
import os
import colorsys
from PIL import Image
import numpy


def main():

    
    input_image = os.path.splitext(sys.argv[1])[0]
    print("image name (without filetype): " + input_image)

    try:

        image = Image.open(sys.argv[1])

        hls_array = create_hls_array(image)

        new_image = image_from_hls_array(hls_array)
        
        new_image_name = str(input_image + "_recreated.jpg")
        
        print(new_image_name)
        

        new_image.save(new_image_name, quality=95)

    except IOError as e:

        print(e)


def create_hls_array(image):

    """
    Creates a numpy array holding the hue, lightness
    and saturation values for the Pillow image.
    """

    pixels = image.load()

    hls_array = numpy.empty(shape=(image.height, image.width, 3), dtype=float)

    for row in range(0, image.height):

        for column in range(0, image.width):

            rgb = pixels[column, row]

            hls = colorsys.rgb_to_hls(rgb[0]/255, rgb[1]/255, rgb[2]/255)

            hls_array[row, column, 0] = hls[0]
            hls_array[row, column, 1] = hls[1]
            hls_array[row, column, 2] = hls[2]

    return hls_array


def image_from_hls_array(hls_array):

    """
    Creates a Pillow image from the HSL array
    generated by the create_hls_array function.
    """

    new_image = Image.new("RGB", (hls_array.shape[1], hls_array.shape[0]))

    for row in range(0, new_image.height):

        for column in range(0, new_image.width):

            rgb = colorsys.hls_to_rgb(hls_array[row, column, 0],
                                      hls_array[row, column, 1],
                                      hls_array[row, column, 2])

            rgb = (int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255))

            new_image.putpixel((column, row), rgb)

    return new_image


main()

print("finished")