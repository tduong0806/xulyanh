import cv2
import numpy as np

# Đọc 2 ảnh
img1 = cv2.imread('level/level_0.png')
img2 = cv2.imread('level/level_3.png')

# Chuyển đổi sang ảnh xám
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Tìm điểm khác biệt giữa 2 ảnh
diff = cv2.absdiff(gray1, gray2)

# Áp dụng bộ lọc Gaussian để làm mờ điểm khác biệt
blur = cv2.GaussianBlur(diff, (7, 7), 7)

# Áp dụng threshold
ret, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Tìm và sửa các điểm khác biệt
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    (x, y, w, h) = cv2.boundingRect(contour)
    center = (int(x + w / 2), int(y + h / 2))
    radius = int(max(w, h) / 2)
    cv2.circle(img1, center, radius, (0, 0, 255), 2)
    cv2.circle(img2, center, radius, (0, 0, 255), 2)


# Nối 2 ảnh theo chiều ngang
result = np.hstack((img1, img2))

# Hiển thị ảnh kết quả
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()