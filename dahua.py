import cv2

# Replace with your IP camera's RTSP stream URL
rtsp_url = "rtsp://admin:T6PePYN!DJg8!h@192.168.1.108/"

# Create a VideoCapture object to capture the RTSP stream
cap = cv2.VideoCapture(rtsp_url)

# Set the buffer size to a reasonable value
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

def process_frame(frame):
    # Perform minimal frame processing here
    # Avoid comple  operations or excessive image manipulation

    # Resize the frame to reduce processing overhead
    frame = cv2.resize(frame, (320, 240), interpolation=cv2.INTER_AREA)

    return frame




# Main streaming loop
while True:
    # Capture a frame
    ret, frame = cap.read()
    # Check if the frame was captured successfully
    if not ret:
        print("Error capturing frame")
        break
    # Process the frame to reduce processing overhead
    processed_frame = process_frame(frame)

    # Display the processed frame
    cv2.imshow('IP Camera Stream', processed_frame)

    # Check if the user wants to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture object
cap.release()

# Close all windows
#cv2.destroyAllWindows()