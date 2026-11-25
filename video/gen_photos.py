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

for i, sc in enumerate(ep.S):
    prompt = sc.get("photo")
    path = f"{OUT}/{i:02d}.png"
    if not prompt or os.path.exists(path):
        continue
    t = time.time()
    g = torch.Generator().manual_seed(sc.get("seed", 1000 + i))
    img = pipe(f"{STYLE}, {prompt}", num_inference_steps=6, guidance_scale=8.0, width=512, height=768,
               generator=g).images[0]
    img.save(path)
    print(f"{i:02d} {time.time() - t:.0f}s {prompt[:70]}", flush=True)
print("done")
