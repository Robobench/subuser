#/bin/bash
apt-get clean
apt-get update
apt-get -y install --force-yes xserver-xorg-core x-window-system libgl1-mesa-glx
apt-get install -y binutils mesa-utils module-init-tools

host_descriptor_file=/subuser/hostdata/host_descriptor.json


ati_version=`cat $host_descriptor_file | grep ati | awk '{print $3}'`
has_ati=`cat $host_descriptor_file | grep ati | awk '{print $3}'| grep "\."`
nvidia_version=`cat $host_descriptor_file | grep nvidia | awk '{print $3}'`
has_nvidia=`cat $host_descriptor_file | grep nvidia | awk '{print $3}'| grep "\."`

if [ $has_nvidia ]; then
    nvidia_bin=/subuser/hostdata/driver.run
    if test ! -f $nvidia_bin; then
	nvidia_driver_uri=http://us.download.nvidia.com/XFree86/Linux-x86_64/${nvidia_version}/NVIDIA-Linux-x86_64-${nvidia_version}.run
	wget -O $nvidia_bin $nvidia_driver_uri
    fi
    sh $nvidia_bin -a -N --ui=none --no-kernel-module -q

    rm $nvidia_bin
fi

if [ $has_ati ]; then
    apt-get install -y fglrx fglrx-dev
fi
    
