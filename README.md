# Augmentor_customizing
Customize Augmentor package

# Customize "Operations.py" and "Pipeline.py"
1. Supplement additional operation.
   - GaussianBlur : perform Gaussian blurring on input image.
   
   - Flip Rotation : expnad a input image with 8 flipped images, rotate the expanded image, and crop the rotated image as its original size
   
   - Flip Rotation GaussianBlur : expnad a input image with 8 flipped images, rotate the expanded image, perform Gaussian blurring on the boundary places between central image and each flipped image, and crop as its original size.
   
   - RandomScale : resize the size of input image by random variable.
   
2. Change original parameters into random variable. 

# How to use

1. Install Augmentor package using pip install. 

2.  Replace "Operations.py" and "Pipeline.py" in original Augmentor package folder to customized files in this resposistory.

