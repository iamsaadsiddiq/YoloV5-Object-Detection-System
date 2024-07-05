import streamlit as st
import subprocess
import threading

# Function to run YOLOv5 detection in a separate thread
def run_detection():
    command = [
        "python", "detect.py",
        "--weights", "yolov5s.pt",
        "--source", "0",  # Use webcam as source
        "--exist-ok",    # Don't increment folder
        "--view-img"     # Show image after detection
    ]
    global process
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while process.poll() is None:
        output = process.stdout.readline().decode().strip()
        if output:
            st.write(output)

# Streamlit app configuration
st.set_page_config(
    page_title="Real-Time Object Detection with YOLOv5",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.title("Real-Time Object Detection with YOLOv5")

st.markdown("""
YOLOv5 is a state-of-the-art real-time object detection model. This Streamlit app demonstrates 
real-time object detection using YOLOv5 with webcam feed. Click 'Start Camera' to begin detection.
""")

# Start and stop camera buttons with animation
start_button = st.button('Start Camera', key='start_button', help="Starts object detection on webcam feed")
stop_button = st.button('Stop Camera', key='stop_button', help="Stops object detection")

if start_button:
    # Start detection in a new thread
    detection_thread = threading.Thread(target=run_detection)
    detection_thread.start()

if stop_button:
    # Terminate the subprocess for camera feed
    if 'process' in globals():
        process.terminate()

# Information about YOLOv5 detection
st.markdown("""
### YOLOv5 Detection Details

YOLOv5 is a fast and efficient object detection model that achieves state-of-the-art performance. It can detect objects in real-time
and is suitable for various applications including surveillance, robotics, and more.
""")
