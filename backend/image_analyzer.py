import base64
from openai import OpenAI
import Database.mongo_db as mongo_db
import json

client = OpenAI()


# Function to encode the image
def encode_image(image_path):
    print("inside encode_image function")
    print(f"Image path: {image_path}")
    try:
        with open(image_path, "rb") as image_file:
            encodedString = base64.b64encode(image_file.read()).decode("utf-8")

        # Path to your image
        # image_path = "path_to_your_image.jpg"

        # Getting the Base64 string
        # base64_image = encode_image(image_path)

        response = client.responses.create(
            model="gpt-4.1",
            input=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text",
                            "text": """
                             i want to know 1. Total 2.merchant name, 3.date 4.category of purchase like grocery or household supplies. Give me the output in Json Format  like this 
                                    {
                                    merchant_name : #CAPITAL LETTERS
                                    date: MM/DD/YYYY
                                    total_cost : only amount do not include currency symbol
                                    item_category: [
                                        {
                                            category: Food & Groceries: 
                                            money_spent :
                                            
                                        },
                                        {
                                            category: Food & Groceries: 
                                            money_spent :
                                        },
                                    ]     
                                }
                             
                             #Give me the output in JSON format.
                             #Group all the items by category and give me the total money spent in each category.
                             """,
                        },
                        {
                            "type": "input_image",
                            "image_url": f"data:image/jpeg;base64,{encodedString}",
                        },
                    ],
                }
            ],
        )

        print(response.output_text)

        response.output_text.find("```json")
        response.output_text.find("```")
        json_output = response.output_text.split("```json")[1].split("```")[0].strip()
        strtojson = json.loads(json_output)
        print("JSON Output by rushi:", json_output)
        print("type")
        print(type(strtojson))
        print("below is the json object")
        print(strtojson)
        print(strtojson.get("merchant_name"))
        mongo_db.get_database()
        mongo_db.get_collection()
        mongo_db.insert_json_output(strtojson)

    except Exception as e:
        print(f"An error occurred while encoding the image: {e}")
