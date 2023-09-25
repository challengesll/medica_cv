from paddleocr import PaddleOCR, draw_ocr

# Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
# 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`

ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # need to run only once to download and load model into memory
img_path = './imgs/6.jpg'
results = ocr.ocr(img_path, cls=True)
for idx in range(len(results)):
    res = results[idx]
    # print(len(res))
    for line in res:
        print(line)
# 显示结果
from PIL import Image
import cv2
import numpy as np

image = Image.open(img_path)
im = np.array(image)
for result in results:

# result = result[0]
    box = np.array(result[0],dtype=np.int32)
    txt = result[1][0]
    score = result[1][1]

    cv2.polylines(im, [np.array(box)], True, (255,0,0), 2)
# cv2.imshow("img", im)
# cv2.waitKey(100000)
# cv2.destroyAllWindows()
image = Image.fromarray(im)
image.save("result6.jpg")

# boxes = [line[0] for line in result]
# txts = [line[1][0] for line in result]
# scores = [line[1][1] for line in result]
# im_show = draw_ocr(image, boxes, txts, scores, font_path='./fonts/simfang.ttf')
# im_show = Image.fromarray(image)
# im_show.save('result.jpg')
