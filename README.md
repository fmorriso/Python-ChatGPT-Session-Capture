# Python example of reading a text file one line at a time.

Find a text file and read it line at a time.

## Tools Used

| Tool    |    Version |
|:--------|-----------:|
| Python  |     3.13.2 |
| PyCharm | 2024.3.4.1 |

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
