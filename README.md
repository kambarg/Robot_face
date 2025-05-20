# 🧭 Let's draw

This is a learning project focused on using the **Qt framework** and **Python** for creating 2D graphical applications.  
It explores both **Qt (via PySide6)** and **Pygame** for building interactive visual experiences — such as robot faces with animated emotions 🤖.

The robot face can now detect and react to faces using your webcam! 📸

---

## 🚀 Quick Start

Follow these steps to get up and running:

1. **Install Python 3**
   ```bash
   sudo apt install python3
   ```

2. **Create and Activate Python Virtual Environment**
   ```bash
   # Create a new virtual environment
   python3 -m venv venv

   # Activate the virtual environment
   source venv/bin/activate

   # Your prompt should change to indicate you're in the virtual environment
   # To deactivate the virtual environment when you're done:
   # deactivate
   ```

3. **Install Required Packages**
   ```bash
   # Make sure your virtual environment is activated
   pip install PySide6 # ?
   pip install pygame # library that is used to draw robot face
   pip install opencv-python # to control usb camera and for haar cascades face detection method
   pip install ultralytics # for yolo8 face detection method
   ```

4. **Run the project**  
   ```bash
   sudo usermod -a -G video $USER
   python3 robot_face_new.py
   ```

5. **Deactivate Python Virtual Environment**

   When you are done, deactivate the virtual environment:
   ```bash
   deactivate
   ```

6. **Troubleshooting Video Camera**

	Check that USB camera is recognized as device in the system: 
	```bash
	ls -l /dev/video* && v4l2-ctl --list-devices
	```
	Your camera should be listed as one of the registered devices 
	/dev/video0, /dev/video1 etc. 

	Than check that camera works:
	```bash
	ffplay /dev/video0
	```
	Verify the camera permisions:
	```bash
	groups $USER | grep video
	```
---

## 🤖 Features

- Fullscreen robot face display
- Webcam face detection
- Interactive eye tracking
- Emotional reactions to detected faces
- Winks when first detecting a face

Feel free to contribute, tweak, or fork this project as I continue exploring cool stuff in Python and graphics! ✨
