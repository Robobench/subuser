#!/bin/bash
# input is host descriptor path
NVIDIA_DIR=/proc/driver/nvidia
ATI_DIR=/dev/ati

nvidia_version=0
ati_version=0
host_descriptor_file=$1/host_descriptor.json

# Get current xorg version
 xorg_version=$(xdpyinfo | grep "X.Org version" | awk '{print $3}')


if test -d $NVIDIA_DIR; then


    if test ! -d $NVIDIA_DIR; then
	echo "NVIDIA driver not installed yet. Driver must be installed on host first"
	return -1
    fi

# Get your current host nvidia driver version, e.g. 340.24
    nvidia_version=$(cat $NVIDIA_DIR/version | head -n 1 | awk '{ print $8 }')


    mkdir -p $1

    
fi

if test -d $ATI_DIR; then
    echo ati
    ati_version=$(LIBGL_DEBUG=verbose fglrxinfo 2>&1 | grep AtiGetClient| awk '{print $3}')
fi

echo "{"> $host_descriptor_file
echo '"nvidia": "' $nvidia_version ' "' >> $host_descriptor_file
echo ',"xorg": "' $xorg_version ' "' >> $host_descriptor_file
echo ',"ati": "' $ati_version ' "'>> $host_descriptor_file
echo "}" >>  $host_descriptor_file
