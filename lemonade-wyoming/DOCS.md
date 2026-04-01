# Lemonade Wyoming — Local Voice Assist for Home Assistant

Run **fully local** voice assistants in Home Assistant using [Lemonade](https://github.com/lemonade-sdk/lemonade) as the AI backend:

| Capability | Backend | Models |
|---|---|---|
| **Speech-to-Text** | Whisper via whisper.cpp or FastFlowLM | Whisper Tiny → Large-v3-Turbo |
| **Conversation / LLM** | LLama.cpp (Vulkan/ROCm/CPU), FastFlowLM (NPU), RyzenAI (NPU) | Qwen 3, Llama 3.2, Phi-4, Mistral 7B |
| **Text-to-Speech** | Kokoro TTS | kokoro-v1 (multiple voices) |

## Prerequisites

1. **Lemonade server** must be installed and accessible from the machine
   running Home Assistant.  Install it from
   <https://github.com/lemonade-sdk/lemonade/releases>.
2. If running Home Assistant OS / Supervised, the Lemonade server should
   run on the **host** (not inside a container).  Set **Lemonade Host** to
   `host.docker.internal` or the host's LAN IP.

## Installation

1. Add this repository URL to your Home Assistant add-on store:
   **Settings → Add-ons → Add-on Store → ⋮ → Repositories**
2. Install the **Lemonade Wyoming** add-on.
3. Open the add-on **Configuration** tab and select your desired models
   and backends.
4. Start the add-on — it will automatically download the selected models
   on first launch.
5. Go to **Settings → Voice assistants** and create / edit an assistant.
   Select *lemonade-whisper* for STT, *lemonade-llm* for Conversation
   Agent, and *lemonade-kokoro* for TTS.

## Configuration Options

### Speech-to-Text

| Option | Default | Description |
|---|---|---|
| STT Model | `Whisper-Large-v3-Turbo` | Whisper model size.  Larger = more accurate but slower. |
| STT Backend | `auto` | `whispercpp:cpu`, `whispercpp:npu`, `whispercpp:vulkan`, or `flm:npu`. |
| STT Language | `en` | ISO 639-1 code or `auto` for detection. |
| STT Beam Size | `0` | Beam search width (`0` = auto). |

### Conversation / LLM

| Option | Default | Description |
|---|---|---|
| LLM Model | `Qwen3-4B-GGUF` | GGUF model for chat completions. |
| LLM Backend | `auto` | `llamacpp:vulkan`, `llamacpp:rocm`, `llamacpp:cpu`, `flm:npu`, `ryzenai:npu`. |
| LLM Context Size | `4096` | Max context window in tokens. |
| LLM Max Tokens | `256` | Max tokens per response. |
| LLM System Prompt | *(built-in)* | Customise the assistant personality. |

### Text-to-Speech

| Option | Default | Description |
|---|---|---|
| TTS Model | `kokoro-v1` | Kokoro ONNX model. |
| TTS Voice | `af_heart` | Voice ID.  `af_` = American Female, `am_` = American Male, `bf_` = British Female, `bm_` = British Male. |

### Connection

| Option | Default | Description |
|---|---|---|
| Lemonade Host | `localhost` | Hostname/IP of the Lemonade server. |
| Lemonade Port | `8000` | HTTP port of the Lemonade server. |
| Auto-start Lemonade | `false` | Try to launch `lemond` if not already running. |

## Standalone Usage (without Home Assistant)

```bash
pip install .
python -m wyoming_lemonade \
    --stt-model Whisper-Large-v3-Turbo \
    --llm-model Qwen3-4B-GGUF \
    --tts-model kokoro-v1 \
    --tts-voice af_heart \
    --lemonade-host localhost \
    --lemonade-port 8000 \
    --debug
```

Then point any Wyoming client at ports **10500** (STT), **10600** (LLM),
**10700** (TTS).

## Ports

| Port | Service |
|---|---|
| 10500 | Wyoming STT (Whisper) |
| 10600 | Wyoming Conversation (LLM) |
| 10700 | Wyoming TTS (Kokoro) |
