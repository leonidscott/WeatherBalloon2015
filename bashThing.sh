#!/bin/bash
date >> flightdata.txt
while true
do
	sudo python finalgpstest.py >> flightdata.txt
done
