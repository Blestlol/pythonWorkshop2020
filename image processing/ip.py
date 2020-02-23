import cv2
img = cv2.imread("galaxy.jpg", 0)

#print(img)
#print(type(img))
#print(img.shape)
#print(img.ndim)

cv2.imshow("galaxy", img)
cv2.waitKey(30000)
cv2.destroyAllWindows
'''
resize_img = cv2.resize(img, (238,288))
cv2.imshow("resizedIMG", resize_img) 
cv2.waitKey(30000)
cv2.destroyAllWindows
'''
'''
r_img = cv2.resize(img, ((int(img.shape[1]/3)), (int(img.shape[0]/3))))
cv2.imshow("resizedIMG", r_img) 
cv2.waitKey(30000)
cv2.destroyAllWindows
cv2.imwrite("GALAXY_resized.jpg", r_img)
'''
'''
lst = []
for i in range(0, 9):
    img = cv2.imread("galaxy({}).jpg".format(i), 1)
    lst.append(img)
    r_img = cv2.resize(lst[i], ((int(lst[i].shape[1]/3)), (int(lst[i].shape[0]/3))))
    cv2.imwrite("GALAXY({}).jpg".format(i), r_img)
    '''