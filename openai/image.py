from dotenv import load_dotenv
import openai
import os
load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]

response = openai.Image.create(
    prompt="a white siamese cat",
    n=1,
    size="1024x1024"
)
image_url = response['data'][0]['url']
print(image_url)
