import cv2

def play_video(video_path):

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error opening video file")
        return

    # Initialize the current frame index
    current_frame = 0

    while True:

        cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame)

        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow('Video Player', frame)

        key = cv2.waitKey(0) & 0xFF

        # If 'q' is pressed, exit the loop
        if key == ord('q'):
            break

        # If 'f' is pressed, go to the next frame
        if key == ord('f'):
            current_frame += 1

        # If 'b' is pressed, go to the previous frame
        if key == ord('b'):
            current_frame -= 1

            # Skip to the beginning if at the first frame
            if current_frame < 0:
                current_frame = 0

    cap.release()
    cv2.destroyAllWindows()

video_path = 'Enter Video Path Here'
play_video(video_path)
