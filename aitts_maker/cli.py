import argparse
import textwrap

from .core import generate_tts


def main():
    print("\n[INFO] Character Limits:")
    print("  - Normal TTS: 3000 characters")
    print("  - AI TTS:     1000 characters\n")
    parser = argparse.ArgumentParser(
        description="Generate TTS MP3s using standard or AI voices from ttsmp3.com",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""\
            Available Normal TTS Languages (3000 chars limit):
              - Arabic, Australian English, Brazilian Portuguese, British English, Canadian French
              - Castilian Spanish, Chinese Mandarin, Danish, Dutch, French, German, Icelandic
              - Indian English, Italian, Japanese, Korean, Mexican Spanish, Norwegian, Polish
              - Portuguese, Romanian, Russian, Swedish, Turkish, US English, US Spanish, Welsh
              - Welsh English

            AI-Based TTS Voices (1000 chars limit):
              - Alloy (female), Ash (male), Coral (female, deeper voice), Echo (male)
              - Fable (female), Onyx (male, deeper voice), Nova (female, soft), Sage (female), Shimmer (female)

            AI Endpoint: https://ttsmp3.com/makemp3_ai.php

            Example Usage:
              tts-maker --msg "Hello world!" --vocal "alloy" --speed "1.50" --output hello.mp3 --ai

            Developed by: DOT-007
        """)
    )

    parser.add_argument("--msg", required=True, help="Text message to convert to speech.")
    parser.add_argument("--vocal", default="alloy", help="Voice model to use (e.g., alloy, ash, shimmer).")
    parser.add_argument("--speed", default="1.00", help="Speed multiplier for AI voices (e.g., 1.00, 1.25).")
    parser.add_argument("--output", default="output.mp3", help="Output filename for the generated MP3.")
    parser.add_argument("--ai", action="store_true", help="Use AI voice models instead of standard voices.")

    AI_VOICES = ["alloy", "ash", "coral", "echo", "fable", "onyx", "nova", "sage", "shimmer"]# ...existing code...

    args = parser.parse_args()

    if not args.ai and args.vocal.lower() in AI_VOICES:
        print(f"[ERROR] The voice '{args.vocal}' is an AI voice model. Please add the --ai flag to use it.")
        return

    if not args.ai and args.speed != "1.00":
        print("[WARNING] Speed adjustment is only supported for AI voices. Ignoring --speed for normal TTS.")

    if args.ai and args.vocal.lower() not in AI_VOICES:
        print(f"[WARNING] The voice '{args.vocal}' is not an AI voice model. Using --ai flag with a normal TTS voice may not work as expected.")

    try:
        result = generate_tts(
            msg=args.msg,
            vocal=args.vocal,
            speed=args.speed,
            output_file=args.output,
            use_ai=args.ai
        )
        print("Saved Successfully to :", args.output, "\nOr Download Link: ", result.get("URL"))
    except Exception as e:
        print("\n[ERROR] TTS generation failed.")
        print("Details:", e)
        print("Issue with API or message format. Try using an AI voice model (with --ai) or check your input text.\n")