from ultralytics import YOLO

model = YOLO("yolov8n.yaml") 

model.train(
    data='images/archive/Processed_Grayscale/data.yaml',
    epochs=100,
    imgsz=640,
    flipud=0.0,         # dikey çevirme (kapalı)
    fliplr=0.5,         # yatay çevirme (yarısına uygula)
    scale=0.5,          # %50 oranında zoom in/out
    translate=0.1,      # %10 kadar kaydırma
    shear=0.0,          # 0.1 civarında verilebilir
    hsv_h=0.015,        # hue değişikliği
    hsv_s=0.7,          # saturation
    hsv_v=0.4,          # brightness
    mosaic=1.0,         # 4 görsel birleştirme (varsayılan)
    mixup=0.2,          # iki görüntüyü birleştir (overfit’e karşı etkili)
    auto_augment='randaugment',  # gelişmiş augment politikası
)
