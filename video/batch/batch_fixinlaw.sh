cd /home/user/claude/video
export HF_HUB_DISABLE_XET=1
until grep -q "NEXT ALL DONE" $SCRATCH/batch_next.log; do sleep 30; done
for ep in inlaw01 inlaw02 inlaw03; do
  python3 $SCRATCH/del_go.py $ep
  export EP=episodes/$ep.py PHOTO_DIR=../output/photos/$ep
  python3 gen_photos.py ../output/photos/$ep 2>&1 | grep --line-buffered -E "^[0-9]|done|Error|Traceback" || true
  VOICE_DIR=$SCRATCH/voice_$ep python3 make_karma.py $SCRATCH/fonts ../output/$ep.mp4
  ffmpeg -y -loglevel error -i ../output/$ep.mp4 -stream_loop -1 -i ../output/bgm/tension.wav -filter_complex "[0:v]setpts=PTS/1.5,fps=30[v];[0:a]atempo=1.5[vo];[vo]asplit[v1][v2];[1:a]volume=0.22[b];[b][v1]sidechaincompress=threshold=0.03:ratio=6:attack=30:release=500[bd];[v2][bd]amix=inputs=2:duration=first:normalize=0[a]" -map "[v]" -map "[a]" -c:v libx264 -crf 20 -pix_fmt yuv420p -c:a aac -b:a 160k -movflags +faststart ../output/$ep-x1.5.mp4
  echo "$ep FIXED"
done
cd ../output
ffmpeg -y -loglevel error -i inlaw01-x1.5.mp4 -i inlaw02-x1.5.mp4 -i inlaw03-x1.5.mp4 -i inlaw04-x1.5.mp4 -filter_complex "[0:v][0:a][1:v][1:a][2:v][2:a][3:v][3:a]concat=n=4:v=1:a=1[v][a]" -map "[v]" -map "[a]" -c:v libx264 -crf 23 -pix_fmt yuv420p -c:a aac -b:a 160k -movflags +faststart inlaw-ep1-4-compilation.mp4
echo "INLAW FIX ALL DONE"
