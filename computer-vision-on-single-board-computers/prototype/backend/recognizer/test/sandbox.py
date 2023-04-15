from vidianiv_people_recognizer import (
    blackbox, 
    CVVideoCapture,
    CVDisplay
)

if __name__ == '__main__':
    blackbox(
        source=CVVideoCapture(0),
        consumer=CVDisplay('Sandbox')
    ).start()
