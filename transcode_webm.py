import cv2

def transcode_to_webm(input_path, output_path):
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        print("Error opening video")
        return False
        
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    fourcc = cv2.VideoWriter_fourcc(*'VP80')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    if not out.isOpened():
        print("Error: Could not initialize VP80 codec.")
        return False
            
    print("Transcoding to VP8 WebM...")
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
    os.rename("media/Test_flight.mp4", "media/Test_flight_temp.mp4")
    success = transcode_to_webm("media/Test_flight_temp.mp4", "media/Test_flight.webm")
    if success:
        os.remove("media/Test_flight_temp.mp4")
