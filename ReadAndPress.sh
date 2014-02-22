# !/bin/bash
python ReadAndPress.py &
zsnes &
STREAM_KEY='live_57134826_alkM6KoRML79i7MZCQQzfnxg4zh9pN'
SERVER="live-fra"    # EU server
# Get Game Window
echo "Click, with the mouse, on the Window that you want to Stream"
rm -f twitch_tmp 2> /dev/null
xwininfo -stats >> twitch_tmp
TOPXY=$(cat twitch_tmp | awk 'FNR == 8 {print $4}')","$(cat twitch_tmp | awk 'FNR == 9 {print $4}')
INRES=$(cat twitch_tmp | awk 'FNR == 12 {print $2}')"x"$(cat twitch_tmp | awk 'FNR == 13 {print $2}')
rm -f twitch_tmp 2> /dev/null
echo " "
ffmpeg -f x11grab -s $INRES -r '16' -i :0.0+$TOPXY -f alsa -i pulse -f flv -ac 1 -ar 44100 -vcodec libx264 -g '16' -keyint_min '16' -b '150k' -minrate '150k' -maxrate '150k' -pix_fmt yuv420p -s '256x224' -preset 'ultrafast' -tune film -acodec libmp3lame -threads '3' -strict normal -bufsize '150k' "rtmp://$SERVER.twitch.tv/app/$STREAM_KEY"