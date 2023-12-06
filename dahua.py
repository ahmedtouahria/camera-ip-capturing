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


net = cv2.dnn.readNet("plate-model/lapi.weights","plate-model/darknet-yolov3.cfg")
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(320,320),scale=1/255) 
frame_counter = 0
frame_skip = 30  # Adjust this value based on your needs

# Main streaming loop
while True:
    # Capture a frame
    ret, frame = cap.read()
        # Skip frames
    frame_counter += 1
    if frame_counter % frame_skip != 0:
        continue

    class_ids,secores,bboxes = model.detect(frame)
    for class_id,score,bboxe in zip(class_ids,secores,bboxes):
        if score >= 0.5:
            x,y,w,h = bboxe
            print("detected")
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