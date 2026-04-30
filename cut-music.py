import argparse
from pathlib import Path


DEFAULT_INPUT = "./media/zui-mei-qing-lv.mp3"
DEFAULT_OUTPUT = "./media/zui-mei-qing-lv-cut.mp3"
DEFAULT_START = "0:08"
DEFAULT_END = "1:37"


def parse_time(value):
    """Convert MM:SS or HH:MM:SS to milliseconds."""
    parts = value.strip().split(":")
    if len(parts) not in (2, 3):
        raise argparse.ArgumentTypeError("time format must be MM:SS or HH:MM:SS")

    try:
        numbers = [int(part) for part in parts]
    except ValueError as exc:
        raise argparse.ArgumentTypeError("time can only contain numbers and colons") from exc

    if any(number < 0 for number in numbers):
        raise argparse.ArgumentTypeError("time cannot be negative")

    if len(numbers) == 2:
        minutes, seconds = numbers
        total_seconds = minutes * 60 + seconds
    else:
        hours, minutes, seconds = numbers
        total_seconds = hours * 3600 + minutes * 60 + seconds

    return total_seconds * 1000


def build_parser():
    parser = argparse.ArgumentParser(description="Cut an MP3 audio clip")
    parser.add_argument("-i", "--input", default=DEFAULT_INPUT, help="input audio file path")
    parser.add_argument("-o", "--output", default=DEFAULT_OUTPUT, help="output audio file path")
    parser.add_argument("-s", "--start", default=DEFAULT_START, help="start time, for example 0:08")
    parser.add_argument("-e", "--end", default=DEFAULT_END, help="end time, for example 1:37")
    return parser


def main():
    args = build_parser().parse_args()
    input_path = Path(args.input)
    output_path = Path(args.output)
    start_ms = parse_time(args.start)
    end_ms = parse_time(args.end)

    if not input_path.exists():
        raise FileNotFoundError(f"input file does not exist: {input_path}")

    if start_ms >= end_ms:
        raise ValueError("start time must be earlier than end time")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    from pydub import AudioSegment

    sound = AudioSegment.from_mp3(input_path)
    clip = sound[start_ms:end_ms]
    clip.export(
        output_path,
        format="mp3",
        tags={"artist": "AppLeU0", "album": output_path.stem},
    )

    print(f"Input: {input_path}")
    print(f"Range: {args.start} ~ {args.end}")
    print(f"Milliseconds: {start_ms} ~ {end_ms}")
    print(f"Output: {output_path}")


if __name__ == "__main__":
    main()
