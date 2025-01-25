# Ortofotomap
We are planning to create a system that enables the modification of camera settings during a drone flight, as well as the creation of both video footage and photos.

Our system is an extension of the Picamera2 WebUI program:
https://github.com/monkeymademe/picamera2-WebUI

## Requirements:
System was tested on the Bookworm version of Raspberry Pi OS (Desktop)

libraries:
- libcamera-apps,
- Picamera2,
- Flask.

# Run program:

    
1. If you're using a virtual environment like kuklok_env, activate it:
```
source kuklok_env/bin/activate
```
2. Navigate to the Project Directory:
```
cd /path/to/picamera2-WebUI
```
3. Run the Webcam Server:
```
python3 app.py
```
4. Access the Server:
Once the server starts, it will  provide a local IP address or port number to access the webcam feed in a browser. For example:
```
http://<your-ip-address>:<port>
```

5. Open this address in a browser to view the feed.

6. Stop the Server (Optional):
Use Ctrl+C in the terminal to stop the server when finished.

# Tecnical debt:

1.  Currently, the recording function works only in Mode: Resolution=(1332, 990), FPS=120.05.
2.  When stopping the recording, streaming also stops, and the program needs to be restarted to resume the live camera feed.
3.  ecordings are saved in the MJPEG format; however, they play back at high speed, making it difficult to interpret the data.


# Other content:

- setup_camera.sh: script to download dependencis when camera isn't available,
- quality_intervalometer: function take a photo with optimal quality,
- fast_intervalometer: function take o photo with optimal frequency.
