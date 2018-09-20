# Augmentor_customizing
Customized Augmentor package

# What's different?
1. Supplement additional operation.
   - GaussianBlur : perform Gaussian blurring on input image.
   
   - Flip Rotation : expnad a input image with 8 flipped images, rotate the expanded image, and crop the rotated image as its original size
   
   - Flip Rotation GaussianBlur : expnad a input image with 8 flipped images, rotate the expanded image, perform Gaussian blurring on the boundary places between central image and each flipped image, and crop as its original size.
   
   - RandomScale : resize the size of input image by random variable.
   
2. Change original parameters into random variable.

3. Add csv_operation module for Augmentor.

# How to install

1. Install Augmentor package using pip install. 
   - pip install Augmentor

2. Replace "Operations.py" and "Pipeline.py" in original Augmentor package folder to customized files in this resposistory.
   - Windows : (Anaconda3 or Anaconda2)/Lib/site-packages/Augmentor
   
   - Linux : (anaconda3 or anaconda2)/lib/(python3.x or python2.x)/site-packages/Augmentor


