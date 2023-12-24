
from openai import OpenAI
import requests
import json
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import base64
import io


def generate_image(values_product):
    client = OpenAI(api_key= "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" )
    response = client.images.generate(prompt = f"build an image that best represents this product based on its fields: {values_product}",
                                    model="dall-e-2",
                                    n=1,
                                    size="512x512",
                                    response_format="b64_json")
    plot_image(response.data[0].b64_json)


def plot_image(image):
    image_data = base64.b64decode(image)
    image= io.BytesIO(image_data)
    with image:
        img = mpimg.imread(image, format='jpeg')
    plt.imshow(img)
    plt.axis("off")
    plt.show()


result = open('result_products.json')
for product in json.load(result):
    generate_image(product)