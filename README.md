# Sign Language to Text Converter

A simple Python application that converts basic hand gestures to text using computer vision.

## Features

- Recognizes 4 gestures: Hello (open palm), Goodbye (closed fist), Yes (thumbs up), No (thumbs down)
- Real-time conversion using webcam input
- Displays recognized text on video feed

## Requirements

- Python 3.7+
- OpenCV
- MediaPipe
- NumPy

## Setup

1. Install required libraries:
   ```
   pip install opencv-python mediapipe numpy
   ```

2. Run the script:
   ```
   python sign_language_converter.py
   ```

## Usage

1. Run the script and allow webcam access.
2. Perform one of the four gestures in front of the camera.
3. The recognized text will appear on the screen.
4. Press 'q' to quit.

## Tips

- Ensure good lighting
- Keep your hand clearly visible to the camera
- Make distinct gestures and hold them steady

## Limitations

- Limited to four basic gestures
- May not work well in poor lighting
- Doesn't recognize complex sign language

For issues or improvements, please open an issue or submit a pull request.