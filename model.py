
from pathlib import Path

import torch
from PIL import Image
from transformers import OwlViTProcessor, OwlViTForObjectDetection


MODEL_DIR = Path(__file__).parent / "models" / "owlvit-base-patch32"

# Load the model and processor from local files only.
processor = OwlViTProcessor.from_pretrained(
    MODEL_DIR,
    local_files_only=True
)

model = OwlViTForObjectDetection.from_pretrained(
    MODEL_DIR,
    local_files_only=True,
    use_safetensors=True
)

model.eval()


def find_object(image: Image.Image, search_term: str, threshold: float = 0.10):
    """
    Detect a searched object in an image using OWL-ViT.

    Returns:
        True if the object is detected, otherwise False.
    """

    if not search_term.strip():
        return False

    image = image.convert("RGB")

    inputs = processor(
        text=[[search_term]],
        images=image,
        return_tensors="pt"
    )

    with torch.no_grad():
        outputs = model(**inputs)

    target_sizes = torch.tensor([image.size[::-1]])

    results = processor.post_process_grounded_object_detection(
        outputs=outputs,
        target_sizes=target_sizes,
        threshold=threshold
    )

    scores = results[0]["scores"]

    return len(scores) > 0
