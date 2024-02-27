import cv2

# Đọc ảnh gốc
anhmau = cv2.imread('images/anhmau.png')
cut_1 = cv2.imread('images/cut_1.png')
cut_2 = cv2.imread('images/cut_2.png')
cut_3 = cv2.imread('images/cut_3.png')


x = 100
y = 100
rows = 300
cols = 300

anhmau[x:x+rows, y:y+cols] = cut_1

x = 200
y = 0
rows = 200
cols = 200


anhmau[x:x+rows, y:y+cols] = cut_2

x = 400
y = 500
rows = 300
cols = 300


anhmau[x:x+rows, y:y+cols] = cut_3
# Hiển thị ảnh kết quả
cv2.imwrite('level/level_2.png', anhmau)
cv2.imshow('level_2', anhmau)
cv2.waitKey(0)
cv2.destroyAllWindows()