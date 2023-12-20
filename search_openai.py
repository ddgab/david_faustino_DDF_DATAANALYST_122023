
from openai import OpenAI
import requests
import json

def search_openai(products):
  client = OpenAI(api_key= "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" )
  search_text  = f'Create a JSON with product segmentation fields such as brand, model, category, subcategory and other features that are useful based on the product title and description. Fields can be text or Boolean, with the aim of grouping and standardizing products based on their specifications. Products: {products}'
  response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    response_format={ "type": "json_object" },
    messages=[
        {"role": "system", "content": "You will receive a list of products with title and description and your task is to categorize the product into various fields based on the keywords."},

      {
        "role": "user",
        "content": search_text
      }
      
    ],
  )
  return json.loads(response.choices[0].message.content.replace("\n",""))["products"]

response = requests.get("https://datasets-server.huggingface.co/first-rows?dataset=spacemanidol%2Fproduct-search-corpus&config=default&split=train")
products = json.loads(response.text)["rows"]
all_products_tract = []
all_products_raw = [{"title":product["row"]["title"].replace("\'",""), "description":product["row"]["text"].replace("\'","")}for product in products]
start = 0
end = 1
while end < len(all_products_raw):
  range = len(str(all_products_raw[start:end]))
# limit do tamanho da mensagem na api é de 25000
  if len(str(all_products_raw[start:end+1])) < 24700:
    end += 1
  else:
    [all_products_tract.append(product) for product in search_openai(all_products_raw[start:end])]
    start = end 
    end += 1
with open("result_products.json", "w") as outfile:
    outfile.write(json.dumps(all_products_tract))

