import requests
import argparse #Pass Command Line Argument to the .py function

parser = argparse.ArgumentParser()
# The order we give to these arguments are the same as the one we use in the CLI
parser.add_argument("language", help="The language of the code we want to generate")
parser.add_argument("prompt", help="What we want the code to do")
parser.add_argument("file", help="The source code file")
args = parser.parse_args()

api_endpoint = "https://api.openai.com/v1/completions"
api_key = "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"

request_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key
}

request_data = {
    "model": "text-davinci-003",
    "prompt": f"Write a {args.language} code to {args.prompt}",
    "max_tokens": 500,
    "temperature": 0.3
}

response = requests.post(api_endpoint, headers=request_headers, json=request_data)

if response.status_code == 200:
    response_text = response.json()["choices"][0]["text"]
    with open(f"{args.file}", "w") as file:
        file.write(response_text)
else:
    print(f"Request Failed with status code: {str(response.status_code)}")
