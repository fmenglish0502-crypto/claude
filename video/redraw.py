"""이상하게 나온 컷만 다시 그리기 (같은 설명, 다른 seed).

사용법: EP=episodes/trash01.py HF_HUB_DISABLE_XET=1 python3 redraw.py <그림폴더> 00_1 05_0 ...
컷 번호 뒤에 :숫자 를 붙이면 그 seed로 그린다 (예: 00_1:77). 없으면 원래 seed + 500.
"""
import importlib.util
import os
import sys

import torch

sys.argv, keys = sys.argv[:2], sys.argv[2:]
OUT = sys.argv[1]
spec = importlib.util.spec_from_file_location("episode", os.environ["EP"])
ep = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ep)

# gen_photos의 모델 준비 부분만 다시 쓰기 위해, 그림 그리는 반복문 앞까지만 실행한다.
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "gen_photos.py")).read()
src = src[: src.index("REF = getattr(ep")]
g = {"__name__": "gen", "sys": sys}
sys.argv = ["gen_photos.py", OUT]
exec(compile(src, "gen_photos.py", "exec"), g)
pipe, STYLE, STEPS, GS, NEG = g["pipe"], g["STYLE"], g["STEPS"], g["GS"], g["NEG"]

for key in keys:
    name, _, seed = key.partition(":")
    i, k = map(int, name.split("_"))
    prompt = ep.S[i]["photos"][k]
    seed = int(seed) if seed else 1000 + i * 10 + k + 500
    kw = {"negative_prompt": NEG} if NEG else {}
    style = STYLE
    if "no people" in prompt and NEG:
        style = "realistic photo, cinematic lighting, sharp focus, high detail, still life, empty scene"
        kw = {"negative_prompt": NEG + ", person, people, woman, man, face, human"}
    img = pipe(f"{style}, {prompt}", num_inference_steps=STEPS, guidance_scale=GS, width=504, height=896,
               generator=torch.Generator().manual_seed(seed), **kw).images[0]
    img.save(f"{OUT}/{name}.png")
    print(name, seed, prompt[:70], flush=True)
