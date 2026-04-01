"""Constants and defaults for wyoming-lemonade."""

from __future__ import annotations

# ── Default ports ────────────────────────────────────────────────────────────
DEFAULT_STT_PORT = 10500
DEFAULT_LLM_PORT = 10600
DEFAULT_TTS_PORT = 10700
DEFAULT_LEMONADE_PORT = 8000
DEFAULT_LEMONADE_HOST = "localhost"

# ── Lemonade API paths ──────────────────────────────────────────────────────
API_PREFIX = "/api/v1"
EP_HEALTH = f"{API_PREFIX}/health"
EP_MODELS = f"{API_PREFIX}/models"
EP_PULL = f"{API_PREFIX}/pull"
EP_LOAD = f"{API_PREFIX}/load"
EP_UNLOAD = f"{API_PREFIX}/unload"
EP_TRANSCRIPTIONS = f"{API_PREFIX}/audio/transcriptions"
EP_CHAT_COMPLETIONS = f"{API_PREFIX}/chat/completions"
EP_SPEECH = f"{API_PREFIX}/audio/speech"

# ── Audio defaults ───────────────────────────────────────────────────────────
WHISPER_SAMPLE_RATE = 16000  # Hz – what Whisper expects
WHISPER_SAMPLE_WIDTH = 2  # 16-bit PCM
WHISPER_CHANNELS = 1  # mono

KOKORO_SAMPLE_RATE = 24000  # Hz – Kokoro's native output rate
KOKORO_SAMPLE_WIDTH = 2  # 16-bit PCM
KOKORO_CHANNELS = 1  # mono

# ── Model registries (curated defaults) ──────────────────────────────────────
STT_MODELS: dict[str, dict] = {
    "Whisper-Tiny": {"size_gb": 0.075, "recipe": "whispercpp"},
    "Whisper-Base": {"size_gb": 0.142, "recipe": "whispercpp"},
    "Whisper-Small": {"size_gb": 0.466, "recipe": "whispercpp"},
    "Whisper-Medium": {"size_gb": 1.42, "recipe": "whispercpp"},
    "Whisper-Large-v3": {"size_gb": 2.87, "recipe": "whispercpp"},
    "Whisper-Large-v3-Turbo": {"size_gb": 1.55, "recipe": "whispercpp"},
}

LLM_MODELS: dict[str, dict] = {
    "Qwen3-0.6B-GGUF": {"size_gb": 0.5, "recipe": "llamacpp"},
    "Qwen3-1.7B-GGUF": {"size_gb": 1.2, "recipe": "llamacpp"},
    "Qwen3-4B-GGUF": {"size_gb": 2.7, "recipe": "llamacpp"},
    "Llama-3.2-1B-Instruct-GGUF": {"size_gb": 0.75, "recipe": "llamacpp"},
    "Llama-3.2-3B-Instruct-GGUF": {"size_gb": 2.0, "recipe": "llamacpp"},
    "Phi-4-mini-instruct-GGUF": {"size_gb": 2.5, "recipe": "llamacpp"},
    "Mistral-7B-Instruct-v0.3-GGUF": {"size_gb": 4.1, "recipe": "llamacpp"},
}

TTS_MODELS: dict[str, dict] = {
    "kokoro-v1": {"size_gb": 0.34, "recipe": "kokoro"},
}

# ── Backend mapping ──────────────────────────────────────────────────────────
# Maps the add-on backend string to Lemonade load-request keys.
# Format: "recipe:device" → dict of extra kwargs for POST /api/v1/load
BACKEND_LOAD_KWARGS: dict[str, dict] = {
    # STT
    "whispercpp:cpu": {"whispercpp_backend": "cpu"},
    "whispercpp:npu": {"whispercpp_backend": "npu"},
    "whispercpp:vulkan": {"whispercpp_backend": "vulkan"},
    "flm:npu": {},  # FLM uses its own recipe
    # LLM
    "llamacpp:vulkan": {"llamacpp_backend": "vulkan"},
    "llamacpp:rocm": {"llamacpp_backend": "rocm"},
    "llamacpp:cpu": {"llamacpp_backend": "cpu"},
    "llamacpp:metal": {"llamacpp_backend": "metal"},
    "ryzenai:npu": {},
}

# ── Misc ─────────────────────────────────────────────────────────────────────
LEMONADE_STARTUP_TIMEOUT = 60  # seconds to wait for lemond to become healthy
LEMONADE_HEALTH_POLL_INTERVAL = 2  # seconds between health-check retries
MODEL_PULL_TIMEOUT = 1800  # 30 min max per model download
