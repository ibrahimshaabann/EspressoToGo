#!/bin/bash

# Get the current date in the format YYYY_MM_DD
current_date=$(date +"%Y_%m_%d")

# Define the filename with the current date
filename="/home/hefny/EspressoToGo/data_${current_date}.dump"

# Run the pg_dump command with the updated filename
# pg_dump -h monorail.proxy.rlwy.net -p 59254 -U postgres -d railway -W -F c -f "$filename"
PGPASSWORD=-*G-AdcfdB-64Dd4D3fbcCDeFCbc3ef* pg_dump -h monorail.proxy.rlwy.net -p 59254 -U postgres -d railway -F c -f "$filename"

