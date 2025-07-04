import cv2 as cv
import sqlite3
from datetime import datetime
from ultralytics import YOLO

# === Yollar ===
VIDEO_PATH = 'images/archive/Sample_Video_HighQuality.mp4'
MODEL_PATH = 'runs/detect/train2/weights/best.pt'  # doğru model yolunla değiştir
DB_PATH = 'detections.db'

# === Veritabanı bağlantısı ===
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

def setup_database():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS detections (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            frame_id INTEGER,
            class_name TEXT,
            x1 INTEGER, 
            y1 INTEGER,
            x2 INTEGER, 
            y2 INTEGER,
            confidence REAL,
            timestamp TEXT
        )
    ''')

# === Modeli yükle ===
model = YOLO(MODEL_PATH)

def detect_and_log():
    cap = cv.VideoCapture(VIDEO_PATH)
    frame_id = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame, conf=0.4, verbose=False)[0]

        for box in results.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            cls_id = int(box.cls[0])
            class_name = model.names[cls_id]
            timestamp = datetime.now().isoformat()

            cursor.execute('''
                INSERT INTO detections (frame_id, class_name, x1, y1, x2, y2, confidence, timestamp)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (frame_id, class_name, x1, y1, x2, y2, conf, timestamp))

            # Görselleştirme
            cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv.putText(frame, f"{class_name} {conf:.2f}", (x1, y1 - 10),
                       cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv.imshow("YOLOv8 Vehicle Detection", frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

        frame_id += 1

    # Tüm işlemler bittiğinde kapat
    conn.commit()
    cap.release()
    conn.close()
    cv.destroyAllWindows()
    print("🎯 All detections logged successfully!")

# === Çalıştır ===
if __name__ == "__main__":
    setup_database()
    detect_and_log()
