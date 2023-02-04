import cv2

img = cv2.imread("Resources/girl.png")
print(img)
cv2.imshow("Output",img)

cv2.waitKey(0)
cv2.destroyAllWindows()