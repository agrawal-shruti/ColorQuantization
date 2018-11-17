import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.utils import shuffle
import imageio
import os
import imageio.core.util

def recreate_image(codebook, labels, w, h):
    """Recreate the (compressed) image from the code book & labels"""
    d = codebook.shape[1]
    image = np.zeros((w, h, d))
    label_idx = 0
    for i in range(w):
        for j in range(h):
            image[i][j] = codebook[labels[label_idx]]
            label_idx += 1
    return image
def root_warning_handler(*args, **kwargs):
    pass
n_colors = [5,50,1000]
img_num=1;
disp =0;
imageio.core.util._precision_warn = root_warning_handler
out_dir = 'quantizedImages'
full_out_dir = 'all_output'
if not os.path.exists(out_dir):
    os.makedirs(out_dir)
    os.makedirs(full_out_dir)
while img_num<4:
# Load the Summer Palace photo
   print(' ')
   i=1;
   disp=disp+1
   image = plt.imread('image'+str(img_num)+'.jpg')
   print('Loaded image'+str(img_num)+'.jpg')
   plt.figure(disp)
   plt.clf()
   plt.axis('off')
   plt.title('Original image' + str(img_num))
   plt.imshow(image)
# Convert to floats instead of the default 8 bits integer coding. Dividing by
# 255 is important so that plt.imshow behaves works well on float data (need to
# be in the range [0-1])

   image = np.array(image, dtype=np.float64) / 255

# Load Image and transform to a 2D numpy array.
   w, h, d = original_shape = tuple(image.shape)
   assert d == 3
   image_array = np.reshape(image, (w * h, d))
   
   for n in n_colors:
      
      print("Fitting model on a small sub-sample of the data")
      image_array_sample = shuffle(image_array, random_state=0)[:1000]
      kmeans = KMeans(n_clusters=n, n_init=10, max_iter=200).fit(image_array_sample)
      print("Done fitting for image " + str(img_num) + " with " +str(n)+ " clusters")

# Get labels for all points
      print("Predicting color indices on the full image (k-means)")
      labels = kmeans.predict(image_array)
      print("Done predicting for image "+ str(img_num) + " with " +str(n)+ " clusters")

# Display all results, alongside original image
      disp=disp+1
      plt.figure(disp)
      plt.clf()
      plt.axis('off')
      plt.title('Quantized image ' + str(img_num) + ' for ' + str(n) + " clusters")
      quant_img = recreate_image(kmeans.cluster_centers_, labels, w, h)
      plt.imshow(quant_img)
      #quant_img = np.array(quant_img, dtype=np.uint8) * 255
      imageio.imwrite(full_out_dir+'\\image'+str(img_num)+'_color_count_'+str(n)+'.jpg', quant_img)
      if n == 1000:
          imageio.imwrite(out_dir+'\\image'+str(img_num)+'_color_count_'+str(n)+'.jpg', quant_img)
      #imageio.imwrite(str(img_num)+str(i)+'.png', quant_img)
      i=i+1
      

   print("Execution Complete for image "+ str(img_num)+"!")
   img_num=img_num+1