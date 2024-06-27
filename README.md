# Gun-detection-using-OpenCV
The "Gun Detection Using OpenCV" project focuses on creating a real-time system that can detect firearms in video streams, such as from a webcam, using computer vision techniques. The system uses the power of OpenCV, a popular open-source computer vision library, to process video frames, detect guns, and provide immediate feedback on the presence of firearms.

Technologies and Libraries Used:

OpenCV:

A comprehensive library for computer vision tasks, used for video capture, image processing, and object detection.
Key functions: cv2.VideoCapture, cv2.CascadeClassifier, cv2.cvtColor, cv2.imshow, and cv2.waitKey.
NumPy:

A library for numerical computing in Python, used here for efficient array operations.
Key function: numpy.array for handling image data.
Imutils:

A library that simplifies basic image processing tasks in OpenCV.
Key function: imutils.resize for resizing video frames.
Pre-trained Haar Cascade Classifier:

An XML file (cascade.xml) containing the trained data for detecting guns using the Haar cascade algorithm -> https://drive.google.com/file/d/1Ndr_HFhxHB8mJ_uysdasXgfAKSQ2is4q/view 
