#/bin/bash
host_descriptor_file=$1
nvidia_version=`cat $host_descriptor_file | grep nvidia | awk '{print $3}'`
nvidia_bin=$2

if test ! -f $nvidia_bin; then
    nvidia_driver_uri=http://us.download.nvidia.com/XFree86/Linux-x86_64/${nvidia_version}/NVIDIA-Linux-x86_64-${nvidia_version}.run
    wget -O $nvidia_bin $nvidia_driver_uri
fi




