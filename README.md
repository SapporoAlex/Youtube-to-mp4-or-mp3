# YouTube to Mp4/Mp3 Downloader
This Python script allows users to download YouTube videos as either Mp4 or Mp3 files. The script prompts the user for a YouTube video URL and offers a simple interface for choosing the download format.

<img src="preview.png" width="400vw" height="auto">

## Features
Download YouTube videos in high-resolution Mp4 format.
Download audio-only Mp3 versions of YouTube videos.
Simple and interactive text-based interface.
Randomly chosen decorative symbols for the interface.
Requirements
- Python 3.x
- Pytube library
- Installation
- Clone the repository:

```bash
git clone https://github.com/yourusername/youtube-downloader.git
cd youtube-downloader
```

## Install the required packages:

```bash
pip install pytube
```

### Set the download path in the script:

Ensure the PATH variable in the script points to your desired download location:

```python
PATH = "C:/Users/..."
```

### Usage
Run the script:

```bash
python youtube_downloader.py
```

### Follow the prompts:

Enter the YouTube video URL.
Choose the download format:
- 1 for Mp4 video
- 2 for Mp3 audio
- 3 to exit

### Example session:
```python
Copy YouTube video URL here: https://www.youtube.com/watch?v=example
╔══════════════════════════╗
☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
☆    𝚈𝚘𝚞𝚝𝚞𝚋𝚎 to Mp4/Mp3   ☆
☆         ❶ 🎞️            ☆
☆         ❷ 🎵            ☆
☆         ❸ ➲            ☆
☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
╚══════════════════════════╝
>>>

```
## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request with any improvements.

## Acknowledgments
Pytube - Python library for downloading YouTube videos
