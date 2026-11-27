cd /home/user/claude/video
export HF_HUB_DISABLE_XET=1
for ep in sim01 sim02 sim03 sim04; do
  until [ -f episodes/$ep.py ]; do sleep 30; done
  export EP=episodes/$ep.py PHOTO_DIR=../output/photos/$ep
  mkdir -p ../output/photos/$ep
  python3 gen_photos.py ../output/photos/$ep 2>&1 | grep --line-buffered -E "^[0-9]|done|Traceback" || true
  python3 tts_karma.py $SCRATCH/voice_$ep > $SCRATCH/tts_$ep.log 2>&1
  VOICE_DIR=$SCRATCH/voice_$ep python3 make_karma.py $SCRATCH/fonts ../output/$ep.mp4
  ffmpeg -y -loglevel error -i ../output/$ep.mp4 -stream_loop -1 -i ../output/bgm/tension.wav -filter_complex "[0:v]setpts=PTS/1.3,fps=30[v];[0:a]atempo=1.3[vo];[vo]asplit[v1][v2];[1:a]volume=0.22[b];[b][v1]sidechaincompress=threshold=0.03:ratio=6:attack=30:release=500[bd];[v2][bd]amix=inputs=2:duration=first:normalize=0[a]" -map "[v]" -map "[a]" -c:v libx264 -crf 20 -pix_fmt yuv420p -c:a aac -b:a 160k -movflags +faststart ../output/$ep-x1.3.mp4
  echo "$ep DONE"
done
echo "SIM ALL DONE"
