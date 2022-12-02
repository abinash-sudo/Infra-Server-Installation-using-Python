#!/bin/bash

echo "Downloading the chef version @@@@chef-version@@@@"
sudo wget https://packages.chef.io/files/stable/chef-server/@@@@chef-version@@@@/amazon/2/chef-server-core-@@@@chef-version@@@@-1.el7.x86_64.rpm > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "Download Successful"
else
    echo "Download failed"
fi

sudo rpm -Uvh chef-server-core-@@@@chef-version@@@@-1.el7.x86_64.rpm
if [ $? -eq 0 ]; then
    echo "Installation Successful"
else
    echo "Installation Failed"
fi

sudo chef-server-ctl reconfigure > /dev/null 2>&1   
if [ $? -eq 0 ]; then
    echo "Installation Successful"
else
    echo "Installation Failed"
fi

#sudo /opt/opscode/bin/knife --version>withoutembeded

#sudo /opt/opscode/embedded/bin/knife --version >withembeded


#sudo chef-server-ctl uninstall > /dev/null 2>&1
sudo rm -rf *





