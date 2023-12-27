from cnocr import CnOcr
ocr = CnOcr()
res = ocr.ocr('image.jpg')
print("Predicted Chars:", res)