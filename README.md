# Python example asking ChatGPt a question

Python example of asking ChatGPt a question and displaying the response.

## Tools Used

| Tool    |  Version |
|:--------|---------:|
| Python  |   3.13.3 |
| openai  |   1.82.1 |
| PyCharm | 2025.1.1 |

## Change History

| Date       | Description                                     |
|:-----------|:------------------------------------------------|
| 2025-03-07 | Initial creation                                |
| 2025-06-01 | put OpenAI secret key in .env file for security |

## References
* [OpenAI Keys](https://platform.openai.com/api-keys)

## Developer Notes

### OpenAI Secret Key Storage
In order to use this program, you need to create ```.env``` text file containing the 
following key/value pair (the value will be different for your situation):

```SECRET_OPENAPI_KEY=some secret key you generated using OpenAI```

### Changes in Function Names

openai.ChatCompletion.create() → client.chat.completions.create()
openai.Image.create() → client.images.generate()
openai.Audio.transcribe() → client.audio.transcriptions.create()
openai.File.create() → client.files.create()
openai.FineTune.create() → client.fine_tuning.jobs.create()

### Output Changes
```python
stream = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Stream this"}],
    stream=True
)
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")

```
