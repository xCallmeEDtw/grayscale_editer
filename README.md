# GrayScale Editer


## 使用套件:
numpy
opencv-python
matplotlib
tk
pillow

下載方式: pip3 -install requirements.txt

## 畫面
* 載入圖片與histogram
![image](https://hackmd.io/_uploads/rkB8HskDeg.png)

* 圖片放大
![image](https://hackmd.io/_uploads/HyQpSsJvgl.png)

* 圖片旋轉
![image](https://hackmd.io/_uploads/Bke1YSskPel.png)


* histogram equalization
![image](https://hackmd.io/_uploads/HkKProkDxx.png)
* bit slicing
![image](https://hackmd.io/_uploads/HkcCBjJwxl.png)

* sharpen
![image](https://hackmd.io/_uploads/ryyf8o1vgx.png)


* 圖片模糊化
![image](https://hackmd.io/_uploads/Hk-W8s1Pxx.png)


## 程式說明:

1. Open/save/display 256-gray-level images in the format of JPG/TIF:
    在 doGui.py中的 OpenFile, SaveFile和SaveAsFile完成
2.  Adjust the contrast/brightness of images:
    (a) 在doImg.py中的linearlyConstrast，透過numpy運算完成實作
    (b) 在doImg.py中的expConstrast，透過numpy運算完成實作
    (c) 在doImg.py中的logConstrast，透過numpy運算完成實作
3. Zoom in and shrink with respect to the images' original size by using bilinear interpolation:
    在Module/ResizeMatrix.py, 透過矩陣乘法，及用for迴圈玩成bilinear interpolation
4. Rotate images by user-deﬁned degrees:
    在Module/RotateMatrix.py和Module/SpinMatrix.py，透過矩陣乘法完成矩陣旋轉，和翻轉矩陣完成特定角度旋轉
5. Gray-level slicing:
    在doImg.py，透過for迴圈完成
6. Display the histogram of images.  An “auto-level” function by using histogram equalization should be provided.:
    在doImg.py，透過matplotlib和openCV套件完成
7. Bit-Plane image:
    在doImg.py，透過for迴圈和二進置判斷完成
8. Smoothing and sharpening:
    在doImg.py，透過手寫filter 和 kernal完成smoothing and sharpening


### doImg.py和Module中的三個程式碼: 
此程式為完成影像處理的主要程式:
1. 透過給定a,b參數，自己實作ax+b,log(ax+b),exp(ax+b)之線性變化
2. 給予特定百分比p(%)，以雙線性插質改變圖片大小，其中Module/ResizeMatrix.py為我自己透過矩陣乘法和，手動實現雙線性插質的程式碼
3. 旋轉特定角度，其中Module/SpinMatrix為翻轉90,180,270之特定角度，而Module/RotateMatrix為把矩陣透過旋轉矩陣做旋轉
4. 自己實做Gray-level slicing
5. 透過openCV和matplotlib實作histogram和auto-level
6. 實作bit-plane slicing
7. 實作filter並實現sharpen和smooth 
### doPhoto.py:
創造一物件，負責儲存圖片的 矩陣(numpy.array), pil的檔案，以及儲存該圖片之Histogram。 並且實作能編輯圖片的方法
### oInput.py:
創造三個物件分別實作輸入視窗，Spinbox視窗，和滑桿視窗
### doGui.py:
創造一物件負責處理GUI和圖片之間的互動, e.g. 開起/儲存檔案，依照作業要求編輯圖片
### hw1.py: 
此為主程式，主要負責開啟GUI介面並呼叫doGui.py中的方法

### GUI 說明:

註: 有些功能可能需要一點時間執行，尤其圖檔較大時, e.g. resize,sharpen,smooth
1. 執行hw1.py可開啟GUI
2. 點開File後open可開啟圖片(histogram會顯示在旁邊), save保存原圖片，save as 可另存圖片
4. 點開Edit後，可以依照對應作業的功能，開啟輸入視窗，在按下confirm後，就會改變圖片
3. Undo可以反回上次的動作，但在open,save,save as執行後，照片的最舊狀態會被並更
