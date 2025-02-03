import nibabel as nib
import matplotlib.pyplot as plt

# Provide the full path to the file
img = nib.load('/Users/Safa/Desktop/1.nii')
data = img.get_fdata()

# Display a slice
slice_index = 50  # Choose a slice number
plt.imshow(data[:, :, slice_index], cmap='gray')
plt.axis('off')
plt.show()
