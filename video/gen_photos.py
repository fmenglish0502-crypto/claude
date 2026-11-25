"""AI 실사 장면 그림 만들기 (LCM_Dreamshaper_v7, MIT 라이선스, CPU).

사용법: EP=episodes/road01.py HF_HUB_DISABLE_XET=1 python3 gen_photos.py <그림폴더>
장면에 photo="영어 설명"이 있으면 <그림폴더>/<장면번호>.png 를 만든다(이미 있으면 건너뜀).
"""
import importlib.util
import os
import sys
import time

import torch
from diffusers import DiffusionPipeline

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
spec = importlib.util.spec_from_file_location("episode", os.environ["EP"])
ep = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ep)

STYLE = getattr(ep, "PHOTO_STYLE", "realistic photo, korean drama still, cinematic lighting, sharp focus, high detail")
torch.set_num_threads(os.cpu_count() or 4)
pipe = DiffusionPipeline.from_pretrained("SimianLuo/LCM_Dreamshaper_v7", safety_checker=None,
                                         requires_safety_checker=False, torch_dtype=torch.float32)
pipe.set_progress_bar_config(disable=True)

REF = getattr(ep, "STYLE", "") == "ref"
W_, H_ = (504, 896) if REF else (512, 768)  # ref 스타일은 화면 꽉 차는 9:16
jobs = []
for i, sc in enumerate(ep.S):
    if sc.get("photo"):
        jobs.append((f"{OUT}/{i:02d}.png", sc["photo"], sc.get("seed", 1000 + i)))
    for k, pr in enumerate(sc.get("photos", [])):  # 빠른 컷: 장면 하나에 그림 여러 장
        jobs.append((f"{OUT}/{i:02d}_{k}.png", pr, 1000 + i * 10 + k))
for path, prompt, seed in jobs:
    if os.path.exists(path):
        continue
    t = time.time()
    g = torch.Generator().manual_seed(seed)
    img = pipe(f"{STYLE}, {prompt}", num_inference_steps=6, guidance_scale=8.0, width=W_, height=H_,
               generator=g).images[0]
    img.save(path)
    print(f"{os.path.basename(path)} {time.time() - t:.0f}s {prompt[:70]}", flush=True)
print("done")
