import sys
import random
from PySide6.QtCore import QObject, Signal, Slot, QTimer
from PySide6.QtWidgets import QApplication
from PySide6.QtQuick import QQuickView
from PySide6.QtCore import QUrl

class EmotionController(QObject):
    emotionChanged = Signal(str)

    def __init__(self):
        super().__init__()
        self.emotions = ["happy", "sad", "surprised"]
        self.timer = QTimer()
        self.timer.timeout.connect(self.change_emotion)
        self.timer.start(3000)  # Change emotion every 3 seconds

    def change_emotion(self):
        new_emotion = random.choice(self.emotions)
        print(f"New emotion: {new_emotion}")
        self.emotionChanged.emit(new_emotion)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = QQuickView()
    context = view.rootContext()

    emotionController = EmotionController()
    context.setContextProperty("emotionController", emotionController)

    view.setSource(QUrl("face.qml"))
    view.show()

    # Connect emotion updates to QML function
    root = view.rootObject()
    emotionController.emotionChanged.connect(root.setEmotion)

    sys.exit(app.exec())