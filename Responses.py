# before
import json
import openai

completion = openai.Completion.create(model='curie')
print(completion['choices'][0]['text'])
print(completion.get('usage'))
print(json.dumps(completion, indent=2))

# after
from openai import OpenAI

client = OpenAI()

completion = client.completions.create(model='curie')
print(completion.choices[0].text)
print(dict(completion).get('usage'))
print(completion.model_dump_json(indent=2))
