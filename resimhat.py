import cv2
import numpy as np
import os
def main():
      # resim aç
imgOriginal = cv2.imread("daireler.png")
if imgOriginal is None: # eğer resim mevcut değilse
print( "hata : resim bulunamadi \n\n") # hata
os.system("pause") # kullanıcı hata mesajını görebilmesi için
return # main fornksiyonundan çıkış programı bitir.
       # Griye dönüştür
imgGrayscale = cv2.cvtColor(imgOriginal, cv2.COLOR_BGR2GRAY)
       # blurla
imgBlurred = cv2.GaussianBlur(imgGrayscale, (5, 5), 0)
       # Canny edges ile şeklin kenarlarını göster
imgCanny = cv2.Canny(imgBlurred, 100, 200)
       # resimleri göster
cv2.imshow("imgOriginal", imgOriginal)
cv2.imshow("imgCanny", imgCanny)
       #klavyeden bir tuşa balılıncaya kadar bekle
cv2.waitKey()
cv2.destroyAllWindows() # bütün pencereleri kapat
return
if __name__ == "__main__":
main()