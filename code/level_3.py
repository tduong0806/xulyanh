import cv2

# Đọc ảnh gốc
anhmau = cv2.imread('images/anhmau.png')
cut_1 = cv2.imread('images/cut_1.png')
cut_2 = cv2.imread('images/cut_2.png')
cut_3 = cv2.imread('images/cut_3.png')


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



chim = cv2.imread('images/chim.png')

# Thay đổi kích thước ảnh chim.jpg
chim_resized = cv2.resize(chim, (100, 100))

# Tạo ROI (Region of Interest) để chèn ảnh chim.jpg vào vị trí mong muốn trong ảnh anhmau.png
rows,cols,channels = chim_resized.shape
x = 0
y = 250
roi = anhmau[x:x+rows, y:y+cols]

# Tạo mask từ ảnh chim_resized để xóa nền của ảnh
chim_gray = cv2.cvtColor(chim_resized,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(chim_gray, 0, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# Áp dụng mask để xóa nền của ảnh chim_resized
anh_chim = cv2.bitwise_and(chim_resized,chim_resized,mask = mask_inv)

# Áp dụng mask_inv để xóa phần tương ứng trong ROI của ảnh anhmau.png
roi_bg = cv2.bitwise_and(roi,roi,mask = mask)

# Thêm ảnh chim_resized đã được xóa nền vào ROI
dst = cv2.add(anh_chim,roi_bg)

# Cập nhật ROI trong ảnh anhmau.png
anhmau[x:x+rows, y:y+cols] = dst

#########################################################

chim = cv2.imread('images/cay.png')

chim_resized = cv2.resize(chim, (100, 100))

rows,cols,channels = chim_resized.shape
x = 219
y = 350
roi = anhmau[x:x+rows, y:y+cols]

chim_gray = cv2.cvtColor(chim_resized,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(chim_gray, 240, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

anh_chim = cv2.bitwise_and(chim_resized,chim_resized,mask = mask_inv)

roi_bg = cv2.bitwise_and(roi,roi,mask = mask)

dst = cv2.add(anh_chim,roi_bg)

anhmau[x:x+rows, y:y+cols] = dst


# Hiển thị ảnh kết quả
cv2.imwrite('level/level_3.png', anhmau)
cv2.imshow('level_3', anhmau)
cv2.waitKey(0)
cv2.destroyAllWindows()