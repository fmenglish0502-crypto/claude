cd /home/user/claude/video
export HF_HUB_DISABLE_XET=1
for ep in sim01 sim02 sim03 sim04; do
  EP=episodes/$ep.py python3 redraw.py ../output/photos/$ep $(cat $SCRATCH/keys_$ep)
  echo "$ep FACE REDRAWN"
done
bash $SCRATCH/rerender.sh sim01 sim02 sim03 sim04
cd /home/user/claude/output
ffmpeg -y -loglevel error -i sim01-x1.3.mp4 -i sim02-x1.3.mp4 -i sim03-x1.3.mp4 -i sim04-x1.3.mp4 -filter_complex "[0:v][0:a][1:v][1:a][2:v][2:a][3:v][3:a]concat=n=4:v=1:a=1[v][a]" -map "[v]" -map "[a]" -c:v libx264 -crf 20 -pix_fmt yuv420p -c:a aac -b:a 160k -movflags +faststart sim-ep1-4-compilation.mp4
echo "FACE COMPILED"
