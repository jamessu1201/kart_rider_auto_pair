import cv2

# 讀取遊戲畫面
img = cv2.imread('screenshot.png')

# 將圖像轉換為灰度
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 使用Canny邊緣檢測算法
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# 使用霍夫變換檢測線段
lines = cv2.HoughLinesP(edges, 1, cv2.PI/180, 100, minLineLength=100, maxLineGap=10)

# 在原圖上繪製線段
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

# 顯示圖像
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()