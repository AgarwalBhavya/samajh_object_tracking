# tracker.py
from deep_sort_realtime.deepsort_tracker import DeepSort

class ObjectTracker:
    def __init__(self):
        self.tracker = DeepSort(max_age=30, n_init=3, max_cosine_distance=0.7)

    def update(self, detections, frame):
        tracks = self.tracker.update_tracks(detections, frame=frame)
        confirmed_tracks = [track for track in tracks if track.is_confirmed()]
        current_ids = set(track.track_id for track in confirmed_tracks)
        return confirmed_tracks, current_ids
