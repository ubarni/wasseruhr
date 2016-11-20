#!/bin/sh 

# Kill all running instances of wasseruhr.py
for i in 1 2 3 4 5
do
  PID=`ps -aef | grep wasseruhr.py | grep -v grep | awk '{print $2}' | head -1`

  if [ "x$PID" != "x" ]; then
    echo "Kill-PID: " $PID
    sudo kill $PID
    sleep .1
  else
    break;
  fi
done

echo "Run Wasseruhr"
sudo python /home/pi/smarthome/wasseruhr/wasseruhr.py &
