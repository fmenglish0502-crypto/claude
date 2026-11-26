cd /home/user/claude/video
export HF_HUB_DISABLE_XET=1
until grep -q "INLAW FIX ALL DONE" $SCRATCH/batch_fixinlaw.log; do sleep 30; done
EP=episodes/trash05.py python3 redraw.py ../output/photos/trash05 00_1 05_1
EP=episodes/trash05.py PHOTO_DIR=../output/photos/trash05 VOICE_DIR=$SCRATCH/voice_trash05 python3 make_karma.py $SCRATCH/fonts ../output/trash05.mp4
ffmpeg -y -loglevel error -i ../output/trash05.mp4 -stream_loop -1 -i ../output/bgm/tension.wav -filter_complex "[0:v]setpts=PTS/1.5,fps=30[v];[0:a]atempo=1.5[vo];[vo]asplit[v1][v2];[1:a]volume=0.22[b];[b][v1]sidechaincompress=threshold=0.03:ratio=6:attack=30:release=500[bd];[v2][bd]amix=inputs=2:duration=first:normalize=0[a]" -map "[v]" -map "[a]" -c:v libx264 -crf 20 -pix_fmt yuv420p -c:a aac -b:a 160k -movflags +faststart ../output/trash05-x1.5.mp4
echo "T5 ALL DONE"
