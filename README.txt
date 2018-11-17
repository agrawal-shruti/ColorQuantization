1> Python version: The code is compiled with python 3.6.5.

2> Packages installed: Following packages are required to run this code.
a> numpy as np
b> matplotlib.pyplot as plt
c> From sklearn.cluster import KMeans
d> From sklearn.utils import shuffle
e> imageio
f> os
g> imageio.core.util

3> Running the source file: This program takes no input. Just running the file color_quantization.py file should produce output.

4> Input: This program works with 3 input images, namely, image1.jpg, image2.jpg, image3.jpg. They are/should be kept in the same directory with the source file.

5> Parameters embedded in the source file: There are 3 k (for k-means algorithm) values used to process these images. They are 5,50,1000.

6> Output folders/directories: There are two output folders/directories. One is all_output and another one is quantizedImages. The former stores all processed images and the later stores processed images for k value 1000. These directories would be created by the program if they do not exist and the files would be overwritten everytime the program is executed. So, it is recommended not to keep a processed image open, before running the program.

7> Output file format: Each processed image would take name of the following format, <original_image_name>_color_count_<k_value>.jpg


