import torch
import cv2
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

img = cv2.imread('Untitled.jpeg')
results = model(img)
results.save()

result = results.pandas().xyxy[0].to_numpy()
reslut = [item for item in result if item[6]=='person']


tmp_img = cv2.imread('Untitled.jpeg')
print('가로 X 세로',tmp_img.shape)

#crpped는 해당 좌표만 가져가겠다 라는 말로 이미지의 minY/maxY, minX/maxX 순서로 잘라서 표시한다 이건 외워야함
cropped = tmp_img[int(result[0][1]):int(result[0][3]), int(result[0][0]):int(reslut[0][2])]

cv2.imwrite('people1.png',cropped)
cv2.rectangle(tmp_img, (int(results.xyxy[0][0][0].item()), int(results.xyxy[0][0][1].item())), (int(results.xyxy[0][0][2].item()), int(results.xyxy[0][0][3].item())),(255,255,255))
cv2.imwrite('result1.png',tmp_img)