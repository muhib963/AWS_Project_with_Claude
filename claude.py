import boto3
import json

prompt_data="write a poem on Genertaive AI"

bedrock=boto3.client(service_name="bedrock-runtime")

payload={
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 512,
    "temperature": 0.5,
    "messages": [
        {
            "role": "user",
            "content": [{"type": "text", "text": prompt_data}],
        }
    ],
}

body = json.dumps(payload)
model_id = "anthropic.claude-3-haiku-20240307-v1:0"  # Replace with your model ID
response = bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json",
)

response_body = json.loads(response.get("body").read())
response_text = response_body.get("content")[0].get("text")
print(response_text)


