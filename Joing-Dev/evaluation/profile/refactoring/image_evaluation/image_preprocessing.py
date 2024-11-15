import PIL
import requests

from PIL import Image
from io import BytesIO

appropriate_image_urls = ['https://i.ytimg.com/vi/389-KHALuxo/sddefault.jpg', 'https://i.ytimg.com/vi/aMKPGl9D_0o/sddefault.jpg', 'https://i.ytimg.com/vi/0p34RJc6AKM/sddefault.jpg', 'https://i.ytimg.com/vi/dBPThakuF08/sddefault.jpg']
inappropriate_image_urls = ['https://i.ytimg.com/vi/kqsqJ0H0S8Y/sddefault.jpg', 'https://i.ytimg.com/vi/LQa6Xx5bZHY/sddefault.jpg', 'https://i.ytimg.com/vi/304B1MQfBIw/sddefault.jpg', 'https://i.ytimg.com/vi/ppjN8aACDfY/sddefault.jpg']

## Getting Image using request from given url
# Getting image from the url
appropriate_response = requests.get(appropriate_image_urls[0])
inappropriate_response = requests.get(inappropriate_image_urls[0])

# Saving it into local
appropriate_img = Image.open(BytesIO(appropriate_response.content))
inappropriate_imag = Image.open(BytesIO(inappropriate_response.content))
appropriate_img_path = appropriate_img.save("./static/test_appropriate.jpg")
inappropriate_img_path  = inappropriate_imag.save("./static/test_inappropriate.jpg")

# Save all of them
image_name = "_appropriate.jpg"
to_static = "./static/"
for i in range(len(inappropriate_image_urls)):
    url = inappropriate_image_urls[i]
    response = requests.get(url=url)
    img = Image.open(BytesIO(response.content))
    img.save(to_static + str(i) + image_name)

## Combining Four images into One Image
image_one = Image.open(to_static + str(0) + image_name)
image_two = Image.open(to_static + str(1) + image_name)
image_three = Image.open(to_static + str(2) + image_name)
image_four = Image.open(to_static + str(3) + image_name)

img_width = image_one.size[0]
img_height = image_one.size[1]

combined_width = img_width*2
combined_height = img_height*2

combined_image = Image.new('RGB', (combined_width, combined_height))

combined_image.paste(image_one,(0,0))
combined_image.paste(image_two,(img_width, 0))
combined_image.paste(image_three,(0, img_height))
combined_image.paste(image_four,(img_width, img_height))

combined_image.save("./static/combined_appropriate.jpg")
