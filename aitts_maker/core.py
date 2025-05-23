import requests
import os

def generate_tts(msg, vocal="alloy", speed="1.00", output_file="output.mp3", use_ai=True):
    """
    Generate TTS audio using ttsmp3.com

    Args:
        msg (str): Message to convert to speech
        vocal (str): Voice/vocal name
        speed (str): Speed multiplier (default is 1.00)
        output_file (str): File to save the MP3
        use_ai (bool): Whether to use AI voice models (True) or standard TTS (False)

    Returns:
        dict: API response containing the MP3 URL and other data
    """
    url = "https://ttsmp3.com/makemp3_ai.php" if use_ai else "https://ttsmp3.com/makemp3_new.php"
    data = {
        "msg": msg,
        "lang": vocal,
        "source": "ttsmp3"
    }
    if use_ai:
        data["speed"] = speed

    response = requests.post(url, data=data)
    if response.status_code != 200:
        raise Exception("Failed to connect to the TTS API")

    result = response.json()
    # API returns 0 for success, or a string or nonzero for error
    if result.get("Error") != 0:
        raise Exception(f"TTS Generation failed: {result}")

    mp3_url = result.get("URL")
    if not mp3_url:
        raise Exception("No MP3 URL returned by API")

    # Download the MP3 file
    r = requests.get(mp3_url)
    if r.status_code == 200:
        with open(output_file, "wb") as f:
            f.write(r.content)
    else:
        raise Exception("Failed to download the MP3")

    return result