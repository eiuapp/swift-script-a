#!/bin/bash
 
for ip in `cat storage-node-ip.txt`;
do 
    echo $ip 
    ping -w 3 $ip 
done

