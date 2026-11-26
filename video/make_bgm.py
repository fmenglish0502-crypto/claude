"""저작권 걱정 없는 직접 만든 드라마 긴장 BGM (wav). 사용법: python3 make_bgm.py ../output/bgm/tension.wav
단조 화음 패드 + 낮은 심장박동 + 가끔 피아노 음. 대사 밑에 깔리도록 부드럽게 만든다."""
import sys, wave
import numpy as np

SR = 44100
BPM = 76
beat = 60 / BPM
bar = beat * 4
# Am - F - Dm - E (긴장감 있는 단조 진행), 4마디씩 반복
CH = [[57, 60, 64], [53, 57, 60], [50, 53, 57], [52, 56, 59]]
bars = 16
N = int(SR * bar * bars)
t = np.arange(N) / SR
out = np.zeros(N)

def f(m): return 440 * 2 ** ((m - 69) / 12)

def env(n, a, r):
    e = np.ones(n); a, r = int(a * SR), int(r * SR)
    e[:a] = np.linspace(0, 1, a); e[-r:] *= np.linspace(1, 0, r); return e

rng = np.random.default_rng(3)
for b in range(bars):
    ch = CH[(b // 1) % 4]
    s, n = int(b * bar * SR), int(bar * SR)
    tt = np.arange(n) / SR
    pad = np.zeros(n)
    for m in ch + [ch[0] - 12]:
        for det in (-0.12, 0.12):  # 살짝 어긋난 두 음으로 따뜻한 소리
            fr = f(m) * 2 ** (det / 12)
            pad += np.sin(2 * np.pi * fr * tt) + 0.3 * np.sin(4 * np.pi * fr * tt)
    out[s:s + n] += 0.05 * pad * env(n, 0.8, 0.8)
    # 심장박동 (둥-둥)
    for k in range(4):
        for off, amp in ((0, 1.0), (0.22, 0.6)):
            p = s + int((k * beat + off) * SR); m = int(0.25 * SR)
            if p + m > N: continue
            tb = np.arange(m) / SR
            out[p:p + m] += 0.35 * amp * np.sin(2 * np.pi * 52 * tb) * np.exp(-tb * 18)
    # 2마디마다 높은 피아노 음 하나
    if b % 2 == 1:
        m = rng.choice(ch) + 12
        p = s + int(2 * beat * SR); L = int(2.5 * SR); tb = np.arange(L) / SR
        L = min(L, N - p)
        out[p:p + L] += 0.12 * (np.sin(2 * np.pi * f(m) * tb[:L]) + 0.4 * np.sin(4 * np.pi * f(m) * tb[:L])) * np.exp(-tb[:L] * 2.2)

out /= np.abs(out).max() * 1.12
st = np.stack([out, np.roll(out, int(0.012 * SR))], 1)  # 약간의 스테레오
with wave.open(sys.argv[1], "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((st * 32767).astype("<i2").tobytes())
print("bgm", N / SR, "s")
