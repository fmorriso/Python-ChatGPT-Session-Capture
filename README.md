# Python example asking ChatGPt a question

ython example asking ChatGPt a question

## Tools Used

| Tool    |  Version |
|:--------|---------:|
| Python  |   3.13.3 |
| openai  |   1.82.1 |
| PyCharm | 2025.1.1 |

## Change History

| Date       | Description                    |
|:-----------|:-------------------------------|
| 2025-03-07 | Initial creation               |

## References
* [OpenAI Keys](https://platform.openai.com/api-keys)

## Developer Notes

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
