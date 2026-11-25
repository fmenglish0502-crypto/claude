"""02편 대사 녹음: Supertonic(오픈소스, 한국어)으로 줄마다 wav를 만들고 길이를 timing.json에 저장.

사용법: HF_HUB_DISABLE_XET=1 python3 tts_karma.py <출력폴더>
"""
import json
import os
import re
import sys
import wave

import numpy as np
from supertonic import TTS

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)

sys.argv = [sys.argv[0], "x", "x"]  # make_karma가 argv를 읽으므로 자리만 채움
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_karma import S  # noqa: E402

# 인물별 목소리 (F=여성, M=남성)
VOICE = {None: "M2", "서연": "F1", "지민": "F2", "할머니": "F5", "회장": "F5", "비서": "M1",
         "행인1": "M3", "행인2": "F4", "지원자1": "M4", "지원자2": "F3",
         "팀장": "M5", "동료1": "M3", "동료2": "F4",
         "사모님": "F3", "태준": "M4", "손님1": "M3", "손님2": "F4",
         "이사1": "M1", "이사2": "F4", "경찰": "M5",
         "기자1": "M3", "기자2": "F4"}
SPEED = {"사모님": 1.08, "태준": 1.1, "팀장": 1.12, "지민": 1.12, "행인1": 1.1, "행인2": 1.1, "할머니": 0.95, "회장": 0.95, None: 1.05}


def speakable(text):
    t = text.replace("ㅋㅋ", "크크").replace("\"", "")
    return t if re.search(r"[가-힣A-Za-z0-9]", t) else None


tts = TTS(auto_download=True)
styles = {}
timing = {}
for si, sc in enumerate(S):
    for li, (spk, text) in enumerate(sc["lines"]):
        say = speakable(text)
        key = f"{si}_{li}"
        if not say:
            continue
        v = VOICE.get(spk, "M3")
        styles.setdefault(v, tts.get_voice_style(v))
        wav, _ = tts.synthesize(say, voice_style=styles[v], lang="ko", speed=SPEED.get(spk, 1.05), total_steps=10)
        wav = np.asarray(wav, dtype=np.float32).reshape(-1)
        sr = tts.sample_rate
        pcm = (np.clip(wav, -1, 1) * 32767).astype(np.int16)
        with wave.open(f"{OUT}/{key}.wav", "wb") as w:
            w.setnchannels(1)
            w.setsampwidth(2)
            w.setframerate(sr)
            w.writeframes(pcm.tobytes())
        timing[key] = len(pcm) / sr
        print(key, spk, f"{timing[key]:.2f}s", say)
json.dump(timing, open(f"{OUT}/timing.json", "w"), ensure_ascii=False, indent=1)
