import cv2
import numpy as np
import os
def main():
camera=PiCamera()
camera.resolution=(640,480)
camera.framerate=32
rawCapture=PiRGBArray(camera,size=(640,480))
#kamera için bekleme
time.sleep(0.1)
for frame in camera.capture_continuous(rawCapture,format=”bgr”,use_video_port=True):
#resimi temsil eden numPy dizisini alıp imgOriginal içine atıyoruz
 imgOriginal=frame.array
       # Griye dönüştür
imgGrayscale = cv2.cvtColor(imgOriginal, cv2.COLOR_BGR2GRAY)
       # blurla
imgBlurred = cv2.GaussianBlur(imgGrayscale, (5, 5), 0)
       # Canny edges ile şeklin kenarlarını göster
imgCanny = cv2.Canny(imgBlurred, 100, 200)
       # resimleri göster
cv2.imshow("imgOriginal", imgOriginal)
cv2.imshow("imgCanny", imgCanny)
       #klavyeden bir tuşa basılıncaya kadar bekle
rawCapture.truncate(0) # birsonraki frame için rawCapture temizliyoruz.
  key=cv2.waitKey(1)&0xFF
  if key == ord(“q”): # klavyeden q tuşuna basılırsa döngüyü sonlandır.
    return
if __name__ == “__main__”:
     main()