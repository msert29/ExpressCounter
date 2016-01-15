#!/bin/bash
# This script will configure Printer80 as a default printer and will 
# print the order.txt file which has just been written by the Express counter 
# GUI program.

echo "----------------------------------"
echo " Configuring the Printer "
echo "----------------------------------"
lpoptions -d Printer80
echo "Sending the data to the printer"
echo "----------------------------------"
lp -d Printer80 order.txt
