import QtQuick 2.15
import QtQuick.Controls 2.15

Rectangle {
    width: 400
    height: 400
    color: "white"

    // Face
    Rectangle {
        id: face
        width: 200
        height: 200
        radius: 100
        color: "yellow"
        anchors.centerIn: parent

        // Eyes
        Rectangle { width: 20; height: 20; radius: 10; color: "black"; x: 60; y: 60; }
        Rectangle { width: 20; height: 20; radius: 10; color: "black"; x: 120; y: 60; }

        // Mouth
        Rectangle {
            id: mouth
            width: 80
            height: 10
            color: "black"
            x: 60
            y: 140
        }
    }

    // Exposed function for Python
    function setEmotion(emotion) {
        if (emotion === "happy") {
            mouth.height = 10;   // Smile
            mouth.y = 140;
        } else if (emotion === "sad") {
            mouth.height = -10;  // Frown
            mouth.y = 150;
        } else if (emotion === "surprised") {
            mouth.width = 40;
            mouth.height = 40;  // Open mouth
            mouth.y = 130;
        }
    }
}