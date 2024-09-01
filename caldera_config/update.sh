#!/bin/bash
cd /home/ali/caldera


sudo docker build . --build-arg WIN_BUILD=true -t caldera:latest

