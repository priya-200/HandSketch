# ✋ Hand Gesture Drawing App 🎨

An interactive hand gesture-based drawing application where you can draw on a virtual canvas using your **index finger** and control gestures such as **fist** to stop drawing or **open hand** to clear the canvas.

---

## 📌 Key Features
- 🖌️ **Draw with Your Index Finger**: Control the canvas with your hand's movement.
- ✊ **Fist Gesture**: Stops the drawing process.
- 👐 **Open Hand Gesture**: Clears the canvas for a fresh start.
- 🟢 **Visual Feedback**: Displays a green circle on the index tip for precise drawing.
- 🖼️ **Canvas Overlay**: See your drawings in real-time on a virtual canvas.

---

## 🛠️ Libraries Used
- **[OpenCV](https://opencv.org/)**: For real-time video capture and image processing.
- **[MediaPipe](https://mediapipe.dev/)**: For robust hand tracking and gesture recognition.
- **[NumPy](https://numpy.org/)**: To handle and manipulate arrays for the canvas.

---

## 🚀 Getting Started

### Prerequisites
Make sure you have the following installed:
- Python 3.7 or higher
- Required libraries (install using the steps below)
---
## 🎥 How It Works
**Track Your Hand:** The app detects your hand using MediaPipe's Hand Tracking model.

**Draw with Gestures:**
- Index Finger Movement: Draws on the canvas.
- Fist Gesture: Stops drawing.
- Open Hand Gesture: Clears the canvas.
- Visual Feedback: A green circle shows the position of your index tip for better precision
---
## ✍️ Future Enhancements:

- 🎨 Add color selection for drawing.
- 🔄 Include gesture to change line thickness.
- 📂 Save drawings as images.
