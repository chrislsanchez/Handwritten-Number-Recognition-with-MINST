#! /bin/sh

### BEGIN INIT INFO
# Provides:	 Camera initialization
# Required-Start:
# Required-Stop:
# Default-Start:		2 3 4 5
# Defaul-Stop:		0 1 6 
# Short-Description: Starts and stops the camera module
# Description: This program starts and stops the camera module using the DT overlay and fbcp command
### END INIT INFO

# If you want a command to always run, put it here

# Carry out specific functions when asked to by the system
case "$1" in
  start)
	echo "Starting Camera"
    	# sudo modprobe fbtft dma & #Starting DMA but not necessary
	sudo modprobe fbtft_device name=sainsmart18 gpios=reset:25,dc:24 speed=16000000 rotate=270 fps=50 &
	sleep 2 #wait for lcd initialization
	fbcp &
	sleep 2  #wait for fbcp initialization
	raspivid -fps 50 -t 99999999 -w 160 -h 90 &
    ;;
  stop)
    echo "Stopping Cammera"
    # pkill raspivid & # Uncomment to stop the camera module. If leave uncomment  will top the process but not shut down
    ;;
  *)
    echo "Usage: /etc/init.d/start_cam.sh {start|stop}"
    exit 1
    ;;
esac

exit 0
