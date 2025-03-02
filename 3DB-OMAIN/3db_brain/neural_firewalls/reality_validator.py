# بناء الكون الكمي 3DB-OMAIN
FROM nvidia/cuda:11.8.0-base-ubuntu22.04

# تركيب المكتبات الكمية
RUN apt-get update && apt-get install -y \
    python3.11 \
    quantum-devkit \
    3db-tensor-core

# نسخ الشفرة الكمية
COPY . /3db_reality
WORKDIR /3db_reality

# تفعيل البيئة الكمية
RUN pip install -r quantum_requirements.txt
CMD ["python3", "-m", "3db_core"]
