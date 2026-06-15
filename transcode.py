import cv2
import sys

def transcode_to_h264(input_path, output_path):
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        print("Error opening video")
        return False
        
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # Use avc1 (H.264)
    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    if not out.isOpened():
        print("Error: Could not initialize avc1 codec.")
        # Fallback to X264
        fourcc = cv2.VideoWriter_fourcc(*'X264')
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
        if not out.isOpened():
            print("Error: Could not initialize X264 codec either.")
            return False
            
    print("Transcoding to H.264...")
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)
        frame_count += 1
        if frame_count % 100 == 0:
            print(f"Transcoded {frame_count} frames...")
            
    cap.release()
    out.release()
    print("Done!")
    return True

if __name__ == "__main__":
    import os
    os.rename("media/Test_flight.mp4", "media/Test_flight_mp4v.mp4")
    success = transcode_to_h264("media/Test_flight_mp4v.mp4", "media/Test_flight.mp4")
    if success:
        os.remove("media/Test_flight_mp4v.mp4")
