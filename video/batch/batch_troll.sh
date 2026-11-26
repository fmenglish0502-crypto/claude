set -e
cd /home/user/claude/video
export HF_HUB_DISABLE_XET=1
until grep -q "ALL3 DONE" $SCRATCH/batch3.log; do sleep 20; done
for e in 1 2 3 4; do
  export EP=episodes/troll0$e.py PHOTO_DIR=../output/photos/troll0$e
  mkdir -p ../output/photos/troll0$e
  python3 gen_photos.py ../output/photos/troll0$e 2>&1 | grep --line-buffered -E "^[0-9]|done|Error|Traceback" || true
  python3 tts_karma.py $SCRATCH/voice_troll0$e > $SCRATCH/tts_troll0$e.log 2>&1
  VOICE_DIR=$SCRATCH/voice_troll0$e python3 make_karma.py $SCRATCH/fonts ../output/troll0$e.mp4
  ffmpeg -y -loglevel error -i ../output/troll0$e.mp4 -stream_loop -1 -i ../output/bgm/tension.wav -filter_complex "[0:v]setpts=PTS/1.5,fps=30[v];[0:a]atempo=1.5[vo];[vo]asplit[v1][v2];[1:a]volume=0.22[b];[b][v1]sidechaincompress=threshold=0.03:ratio=6:attack=30:release=500[bd];[v2][bd]amix=inputs=2:duration=first:normalize=0[a]" -map "[v]" -map "[a]" -c:v libx264 -crf 20 -pix_fmt yuv420p -c:a aac -b:a 160k -movflags +faststart ../output/troll0$e-x1.5.mp4
  echo "TROLL$e DONE"
done
echo TROLL ALL DONE
