import keras_ocr 

pipeline = keras_ocr.pipeline.Pipeline()

images = [
    keras_ocr.tools.read(img) for img in [
        '/home/anonimouz/Documents/python projects/content/test.jpg',        
        '/home/anonimouz/Documents/python projects/content/test2.png'
    ]
]

print(images[0])
print(images[1])

pred_g = pipeline.recognize(images)

pred_img1 = pred_g[0]
for text, box in pred_img1:
    print(text)
    
pred_img2 = pred_g[1]
for text, box in pred_img2:
    print(text)