# Tugas Pengolahan Citra Convex Hull Transformation 

| NIM | Nama |
| - | - |
| 312210267 | Dimas Firmansyah |

# Penjelasan
### 1. Langkah pertama kita import library yang diperlukan
jika belum memiliki library tersebut silahkan install dengan cara python -m pip install(nama pakacge)
```
import streamlit as st
import matplotlib.pyplot as plt
from skimage.morphology import convex_hull_image
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.util import invert
from PIL import Image
import numpy as np
```
### 2. Membuat widget untuk mengunggah file gambar dengan format PNG, JPG, atau JPEG
```
uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])
```

### 3. Memproses gambar yang di upload
```
if uploaded_file is not None:
    image= Image.open(uploaded_file).convert('RGB')
```

### 4. Konversi gambar ke array numpy
```
    image = np.array(image)
```

### 5. Konversi gambar ke grayscale dan inversi warna
```
    image_gray = rgb2gray(image)
    image_inverted = invert(image_gray)
```

### 6. Menerapkan convex hull
```
    chull = convex_hull_image(image_inverted)
```

### 7. Plotting gambar asli dan hasil transformasi
```
    fig, axes = plt.subplots(1, 2, figsize=(8, 4))
    ax = axes.ravel()

    ax[0].set_title('original')
    ax[0].imshow(image_gray, cmap=plt.cm.gray)
    ax[0].set_axis_off()

    ax[1].set_title('transformed')
    ax[1].imshow(chull, cmap=plt.cm.gray)
    ax[1].set_axis_off()

    plt.tight_layout()
    st.pyplot(fig)
```

### 8. Menjalankan Project
ketik ini pada cmd/terminal anda
```
streamlit run app.py
```

### 9. Hasil Projek
![Screenshot (398)](https://github.com/DimasF3009/Pengolahan-Citra-7/assets/115356128/58454322-c62d-40df-8084-5b55f28d01cb)




