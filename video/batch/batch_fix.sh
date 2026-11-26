cd /home/user/claude/video
export HF_HUB_DISABLE_XET=1
until grep -q "TROLL ALL DONE" $SCRATCH/batch_troll.log; do sleep 30; done
EP=episodes/troll01.py python3 redraw.py ../output/photos/troll01 00_0 00_1 02_0
EP=episodes/troll03.py python3 redraw.py ../output/photos/troll03 00_0 00_1 15_0
for ep in troll01 troll03; do
  EP=episodes/$ep.py PHOTO_DIR=../output/photos/$ep VOICE_DIR=$SCRATCH/voice_$ep python3 make_karma.py $SCRATCH/fonts ../output/$ep.mp4
  ffmpeg -y -loglevel error -i ../output/$ep.mp4 -stream_loop -1 -i ../output/bgm/tension.wav -filter_complex "[0:v]setpts=PTS/1.5,fps=30[v];[0:a]atempo=1.5[vo];[vo]asplit[v1][v2];[1:a]volume=0.22[b];[b][v1]sidechaincompress=threshold=0.03:ratio=6:attack=30:release=500[bd];[v2][bd]amix=inputs=2:duration=first:normalize=0[a]" -map "[v]" -map "[a]" -c:v libx264 -crf 20 -pix_fmt yuv420p -c:a aac -b:a 160k -movflags +faststart ../output/$ep-x1.5.mp4
done
echo "FIX RENDER DONE"
cd ../output
ffmpeg -y -loglevel error -i troll01-x1.5.mp4 -i troll02-x1.5.mp4 -i troll03-x1.5.mp4 -i troll04-x1.5.mp4 -filter_complex "[0:v][0:a][1:v][1:a][2:v][2:a][3:v][3:a]concat=n=4:v=1:a=1[v][a]" -map "[v]" -map "[a]" -c:v libx264 -crf 23 -pix_fmt yuv420p -c:a aac -b:a 160k -movflags +faststart troll-ep1-4-compilation.mp4
echo "FIX ALL DONE"
