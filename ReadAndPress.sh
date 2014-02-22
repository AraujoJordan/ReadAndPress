# !/bin/bash
python ReadAndPress.py &
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
ffmpeg -f x11grab -s $INRES -r '24' -i :0.0+$TOPXY -f alsa -i pulse -f flv -ac 2 -ar 22100 -vcodec libx264 -g '60' -keyint_min '30' -b '1000k' -minrate '1000k' -maxrate '1000k' -pix_fmt yuv420p -s '800x600' -preset 'ultrafast' -tune film -acodec libmp3lame -threads '4' -strict normal -bufsize '1000k' "rtmp://$SERVER.twitch.tv/app/$STREAM_KEY"