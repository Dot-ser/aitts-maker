# AITTS-Maker

Generate TTS (Text-to-Speech) MP3s using standard and AI-based voices from [ttsmp3.com](https://ttsmp3.com).

> ⚠️ This library uses **web scraping** to interact with [ttsmp3.com](https://ttsmp3.com), as there is no official public API. Use responsibly and according to their terms of service.

---

## 📦 Installation

Install via pip:

```sh
pip install aitts-maker
````

---

## ✨ Features

* Supports both standard and AI-powered TTS voices
* Outputs high-quality MP3 files
* Easy-to-use CLI interface

---

## 🎙️ AI-Based TTS Voices (1000-character limit)

API Endpoint: [`https://ttsmp3.com/makemp3_ai.php`](https://ttsmp3.com/makemp3_ai.php)

**Available AI Voice Models:**

* `--vocal alloy` – Alloy (female)
* `--vocal ash` – Ash (male)
* `--vocal coral` – Coral (female, deeper voice)
* `--vocal echo` – Echo (male)
* `--vocal fable` – Fable (female)
* `--vocal onyx` – Onyx (male, deeper voice)
* `--vocal nova` – Nova (female, soft voice)
* `--vocal sage` – Sage (female)
* `--vocal shimmer` – Shimmer (female)

---
```sh
aitts-maker --msg "Hello world!" --vocal alloy --speed "1.50" --output hello.mp3 --ai
```

## 🌐 Standard TTS Voice Options (3000-character limit)

**Available Standard Voices:**

* `--vocal Zeina` – Arabic
* `--vocal Nicole` – Australian English (female)
* `--vocal Russell` – Australian English (male)
* `--vocal Ricardo` – Brazilian Portuguese (male)
* `--vocal Camila` – Brazilian Portuguese (female)
* `--vocal Vitoria` – Brazilian Portuguese (female)
* `--vocal Brian` – British English (male)
* `--vocal Amy` – British English (female)
* `--vocal Emma` – British English (female)
* `--vocal Chantal` – Canadian French (female)
* `--vocal Enrique` – Castilian Spanish (male)
* `--vocal Lucia` – Castilian Spanish (female)
* `--vocal Conchita` – Castilian Spanish (female)
* `--vocal Zhiyu` – Chinese Mandarin (female)
* `--vocal Naja` – Danish (female)
* `--vocal Mads` – Danish (male)
* `--vocal Ruben` – Dutch (male)
* `--vocal Lotte` – Dutch (female)
* `--vocal Mathieu` – French (male)
* `--vocal Celine` – French (female)
* `--vocal Lea` – French (female)
* `--vocal Vicki` – German (female)
* `--vocal Marlene` – German (female)
* `--vocal Hans` – German (male)
* `--vocal Karl` – Icelandic (male)
* `--vocal Dora` – Icelandic (female)
* `--vocal Aditi` – Indian English (female)
* `--vocal Raveena` – Indian English (female)
* `--vocal Giorgio` – Italian (male)
* `--vocal Carla` – Italian (female)
* `--vocal Bianca` – Italian (female)
* `--vocal Takumi` – Japanese (male)
* `--vocal Mizuki` – Japanese (female)
* `--vocal Seoyeon` – Korean (female)
* `--vocal Mia` – Mexican Spanish (female)
* `--vocal Liv` – Norwegian (female)
* `--vocal Jan` – Polish (male)
* `--vocal Maja` – Polish (female)
* `--vocal Ewa` – Polish (female)
* `--vocal Jacek` – Polish (male)
* `--vocal Cristiano` – Portuguese (male)
* `--vocal Ines` – Portuguese (female)
* `--vocal Carmen` – Romanian (female)
* `--vocal Tatyana` – Russian (female)
* `--vocal Maxim` – Russian (male)
* `--vocal Astrid` – Swedish (female)
* `--vocal Filiz` – Turkish (female)
* `--vocal Kimberly` – US English (female)
* `--vocal Ivy` – US English (female)
* `--vocal Kendra` – US English (female)
* `--vocal Justin` – US English (male)
* `--vocal Joey` – US English (male)
* `--vocal Matthew` – US English (male)
* `--vocal Salli` – US English (female)
* `--vocal Joanna` – US English (female)
* `--vocal Penelope` – US Spanish (female)
* `--vocal Lupe` – US Spanish (female)
* `--vocal Miguel` – US Spanish (male)
* `--vocal Gwyneth` – Welsh (female)
* `--vocal Geraint` – Welsh English (male)

---

## 🛠️ CLI Usage Example

```sh
aitts-maker --msg "Hello world!" --vocal "Enrique" --output hello.mp3 
```

**Options:**

* `--msg` – Text to convert to speech
* `--vocal` – Voice model (e.g., alloy, amy, mizuki)
* `--speed` – Speed multiplier for AI voices (e.g., 1.00, 1.25)
* `--output` – Output MP3 filename
* `--ai` – Use AI voice model

---

## 🧩 Python Library Usage

You can also use AITTS-Maker in your Python code:

### While using ai Models
```python
from aitts_maker import generate_tts

result = generate_tts(
    msg="Hello world!",
    vocal="alloy",
    speed="1.25",
    output_file="hello.mp3",
    use_ai=True
)
print("MP3 URL:", result.get("URL"))
```


### While using Normal Models
```python
from aitts_maker import generate_tts

result = generate_tts(
    msg="Hello world!",
    vocal="alloy",
    output_file="hello.mp3",
)
print("MP3 URL:", result.get("URL"))
```
---

## 👤 Author

**DOT-007**
Made with ❤️ by [DOT-007(https://alosiousbenny.vercel.app)]

