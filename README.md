# YOLO-OpenCV Object Detection

Bu proje, **YOLOv8** ve **OpenCV** kullanarak video verileri üzerinde nesne tespiti yapar. Eğitimli YOLO modeli ile yapılan tespitler, video karelerinde görselleştirilir ve tespit sonuçları SQLite veritabanına kaydedilir. Ayrıca proje, Docker üzerinden kolay çalıştırılabilir hale getirilmiştir.

---

## 📁 Proje Yapısı

```bash
YOLO-OPENCV/
├── images/
│   └── archive/
│       ├── No_Apply_Grayscale/
│       └── Processed_Grayscale/
├── runs/                         # YOLO inference çıktı klasörü
├── Sample_Video_HighQuality.mp4
├── Sample_Video_LowQuality.mp4
├── detect_and_log.py            # Ana tespit ve kayıt betiği
├── automatic.py                 # Otomatik tespit süreci
├── query.py                     # Veritabanı sorguları
├── train.py                     # YOLOv8 eğitim betiği
├── detections.db                # Tespitlerin kaydedildiği veritabanı
├── yolo11n.pt                   # Eğitilmiş YOLOv8 model ağırlığı
├── requirements.txt             # Gerekli Python bağımlılıkları
├── Dockerfile                   # Docker container yapılandırması
└── .gitignore

Önce sanal ortam oluşturup bağımlılıkları yükleyin:

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt