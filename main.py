# main.py
from core.detector import YOLODetector
from core.tracker import ObjectTracker
from core.utils import draw_tracks, measure_fps, save_frame_sample
from core.video_io import init_video_input, init_video_output
import cv2

# Initialize detector and tracker
detector = YOLODetector()
tracker = ObjectTracker()

cap = init_video_input('input_video.mp4')
out, frame_size = init_video_output(cap, 'output/output_video.mp4')

frame_idx = 0
fps_list = []
tracked_ids = {}

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    fps_start = measure_fps()

    detections = detector.detect(frame)
    tracks, current_ids = tracker.update(detections, frame)

    # Detect new and missing objects
    for obj_id in list(tracked_ids.keys()):
        if obj_id not in current_ids and frame_idx - tracked_ids[obj_id] > 30:
            print(f'Missing Object ID: {obj_id}')

    for new_id in current_ids:
        if new_id not in tracked_ids:
            print(f'New Object Detected: ID {new_id}')
            tracked_ids[new_id] = frame_idx

    draw_tracks(frame, tracks)
    fps = measure_fps(fps_start)
    fps_list.append(fps)
    cv2.putText(frame, f"FPS: {fps:.2f}", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    if frame_idx % 150 == 0:
        save_frame_sample(frame, frame_idx)

    out.write(frame)
    cv2.imshow('Real-Time Tracking', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    frame_idx += 1

cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Average FPS: {sum(fps_list) / len(fps_list):.2f}")
