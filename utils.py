# utils.py
import cv2
import os
import time

os.makedirs("output/sample_frames", exist_ok=True)

def draw_tracks(frame, tracks):
    for track in tracks:
        l, t, w, h = track.to_ltrb()
        track_id = track.track_id
        cv2.rectangle(frame, (int(l), int(t)), (int(l + w), int(t + h)), (0, 255, 0), 2)
        cv2.putText(frame, f'ID: {track_id}', (int(l), int(t - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

def measure_fps(start_time=None):
    if start_time is None:
        return time.time()
    return 1.0 / (time.time() - start_time)

def save_frame_sample(frame, idx):
    path = f"output/sample_frames/frame_{idx}.jpg"
    cv2.imwrite(path, frame)
