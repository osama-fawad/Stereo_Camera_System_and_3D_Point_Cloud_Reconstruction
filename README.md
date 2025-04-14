# 📷 Stereo Camera System & 3D Point Cloud Reconstruction

This repository contains a complete pipeline for stereo camera calibration, image rectification, and 3D point cloud generation using Python and OpenCV.

---

## Project Structure

### `calibration_photos/left/` & `calibration_photos/right/`
- Contains **checkerboard calibration images** for the **left** and **right** cameras respectively.
- Image files should be named correspondingly (e.g., `left_0.jpg`, `right_0.jpg`).

### `1_capture_multi_camera_images.py`
- Opens **two connected webcams** and captures images from both **simultaneously**.
- Shows a **side-by-side live preview** of both cameras.
- Press **`s`** to save a pair, or **`q`** to quit.
- Saves full-resolution images and resizes only for display.

### `2-stereo_calibration.ipynb`
- Performs **intrinsic calibration** of both cameras.
- Then performs **stereo calibration** to calculate `R`, `T`, `E`, and `F` matrices.
- Also generates and saves remap matrices and `Q` matrix for 3D reconstruction.
- Stores all results in `stereo_calibration.npz`.

### `3-Stereo_Rectification.ipynb`
- Loads the stereo calibration file.
- Rectifies a test image pair using `cv2.remap`.
- Displays rectified outputs with horizontal alignment.

### `Stereo_Camera_Project_Report_Draft.pdf`
- The report for this project
- Contains overall information on such stereo systems taken from various articles and papers
- Draft version - yet to be finalised

## Coming Soon
- 3D point cloud generation using disparity maps
- Streamlit frontend for live capture and visualization
- LFS support for heavy models or notebooks

