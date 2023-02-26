import requests
import openai
import json

class ImageGeneration:
    def __init__(self, api_key_file):
        with open(api_key_file) as f:
            config = json.load(f)
        # Set the OpenAI API key
        openai.api_key = config["api_key"]

    def generate_image(self, prompt, model="image-alpha-001", num_images=1, size="512x512", response_format="url", output_file="generated_image.png"):
        # Set the prompt and parameters for image generation
        data = {
            "model": model,
            "prompt": prompt,
            "num_images": num_images,
            "size": size,
            "response_format": response_format
        }

        # Make a request to the API
        response = openai.Image.create(**data)

        # Get the generated image URL from the response
        image_url = response["data"][0]["url"]

        # Download the generated image
        image_data = requests.get(image_url).content

        # Save the image to disk
        with open(output_file, "wb") as f:
            f.write(image_data)



if __name__ == "__main__":
    image_gen = ImageGeneration("keys.json")
    image_gen.generate_image("an illustration of a cat riding a bicycle in illusional way", output_file="cat_on_bicycle.png")

