
from pathlib import Path
from transformers import OwlViTProcessor, OwlViTForObjectDetection

MODEL_NAME = "google/owlvit-base-patch32"
MODEL_DIR = Path("models/owlvit-base-patch32")


def download_model():
    print("Downloading OWL-ViT model...")

    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    processor = OwlViTProcessor.from_pretrained(MODEL_NAME)
    model = OwlViTForObjectDetection.from_pretrained(
        MODEL_NAME,
        use_safetensors=True
        )

    processor.save_pretrained(MODEL_DIR)
    model.save_pretrained(MODEL_DIR, safe_serialization=True)

    print("Model downloaded and saved successfully!")
    print(f"Model location: {MODEL_DIR}")


if __name__ == "__main__":
    download_model()
