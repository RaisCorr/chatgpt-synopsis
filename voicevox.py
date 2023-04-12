import requests
import json
import wave
from time import sleep
from io import BytesIO

import pyaudio


def post_audio_query(text: str) -> dict:
    """
    Generates a VOICEVOX query.

    :param text: a string containing the text to be converted
    """
    params = {"text": text, "speaker": 0}
    res = requests.post("http://127.0.0.1:50021/audio_query", params=params)
    return res.json()


def post_synthesis(audio_query_response: dict) -> bytes:
    """
    Performs audio synthesis using VOICEVOX.

    :param audio_query_response (dict): A dictionary containing the audio query response.
    :return bytes: The audio content of the synthesized voice.
    """
    params = {"speaker": 0}
    headers = {"content-type": "application/json"}

    # Convert audio query response to JSON format
    audio_query_response_json = json.dumps(audio_query_response)

    # Send POST request to VOICEVOX API
    res = requests.post(
        "http://127.0.0.1:50021/synthesis",
        data=audio_query_response_json,
        params=params,
        headers=headers,
    )

    return res.content


def play_wavfile(wav_file: bytes):
    """
    Play a WAV file using PyAudio library.

    :param wav_file: a bytes object containing the WAV file data
    """
    # Open the WAV file
    wr: wave.Wave_read = wave.open(BytesIO(wav_file))

    # Initialize PyAudio object
    p = pyaudio.PyAudio()

    # Open an audio stream
    stream = p.open(
        format=p.get_format_from_width(wr.getsampwidth()),
        channels=wr.getnchannels(),
        rate=wr.getframerate(),
        output=True,
    )

    # Set the buffer chunk size for reading the data
    chunk = 1024

    # Read the audio data and write it to the output stream until the end of the file
    data = wr.readframes(chunk)
    while data:
        stream.write(data)
        data = wr.readframes(chunk)

    sleep(0.5)
    stream.close()
    p.terminate()


def text_to_voice(text: str):
    """
    Convert input text to speech using VOICEVOX.

    :param text: a string containing the text to be converted
    """
    res = post_audio_query(text)
    wav = post_synthesis(res)
    play_wavfile(wav)
