import torch
import sys
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline


def run_model_on_file(data, model="openai/whisper-large-v3-turbo"):
    device = "cuda:0" if torch.cuda.is_available() else "cpu"

    torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

    model_id = "openai/whisper-large-v3-turbo"

    model = AutoModelForSpeechSeq2Seq.from_pretrained(
        model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
    )

    model.to(device)

    processor = AutoProcessor.from_pretrained(model_id)

    pipe = pipeline(
        "automatic-speech-recognition",
        model=model,
        tokenizer=processor.tokenizer,
        feature_extractor=processor.feature_extractor,
        torch_dtype=torch_dtype,
        device=device,
    )

    result = pipe(data)
    return result


if __name__ == "__main__":

    data = sys.argv[1]
    print(data)

    print("--- Running Whisper ---")
    result = run_model_on_file(data)
    with open(f"{data}_transcript.txt", "w") as output:
        output.write(result["text"])
        print("--- Saved transcript ---")

    print(result["text"])
