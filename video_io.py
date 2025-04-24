# video_io.py
import cv2

def init_video_input(input_path):
    return cv2.VideoCapture(input_path)

def init_video_output(cap, output_path):
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))
    return out, (width, height)
