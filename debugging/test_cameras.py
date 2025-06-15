from lerobot.common.cameras.opencv.configuration_opencv import OpenCVCameraConfig
from lerobot.common.cameras.opencv.camera_opencv import OpenCVCamera
from lerobot.common.cameras.configs import ColorMode, Cv2Rotation
import matplotlib.pyplot as plt

def plot_frame(frame):
        # Plotting the first frame
    plt.figure(figsize=(10, 6))
    plt.imshow(frame)
    plt.title("Camera frame")
    plt.axis("off")
    plt.show()

def main():
# List to store frames
    frames = []

    # Construct an `OpenCVCameraConfig` with your desired FPS, resolution, color mode, and rotation.
    config = OpenCVCameraConfig(
        index_or_path=0,
        fps=15,
        width=640,
        height=480,
        color_mode=ColorMode.RGB,
        rotation=Cv2Rotation.NO_ROTATION
    )

    # Instantiate and connect an `OpenCVCamera`, performing a warm-up read (default).
    camera = OpenCVCamera(config)
    camera.connect()

    # Read frames asynchronously in a loop via `async_read(timeout_ms)`
    try:
        for i in range(10):
            frame = camera.async_read(timeout_ms=200)
            print(f"Async frame {i} shape:", frame.shape)
            frames.append(frame)
            plot_frame(frame)
    finally:
        camera.disconnect()
    

if __name__ == "__main__": 
    main()
