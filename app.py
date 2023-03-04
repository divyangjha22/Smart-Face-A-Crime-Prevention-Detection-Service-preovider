from flask import Flask, render_template
import cv2
app = Flask(__name__)
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)