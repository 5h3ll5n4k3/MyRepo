#!/bin/bash
# Author: sh3ll5n4k3
# HostBuster Version: 1.0
# Description: This tool is made to enumerate subdomains specifically for CTF machines 

# Arguments
DOMAIN=$1
WORDLIST=$2
IP=$3
VERBOSE=$4

# Temporary hosts file
TMP_HOSTS="/tmp/temp_hosts"

# Function to cleanup hosts file
cleanup() {
    if [ -f $TMP_HOSTS ]; then
        tput setaf 3; echo "Cleaning up /etc/hosts..."; tput sgr0
        sudo cp $TMP_HOSTS /etc/hosts
        sudo rm -f $TMP_HOSTS
    fi
}

# Function to check and cleanup on script exit or interruption
check_and_cleanup() {
    if [ -f $TMP_HOSTS ]; then
        cleanup
    fi
}

# Trap to check and cleanup on script exit or interruption
trap check_and_cleanup EXIT

# Display banner
tput setaf 4
figlet -f slant "HostHunter"
tput sgr0

# Backup original /etc/hosts
if sudo cp /etc/hosts $TMP_HOSTS; then
    tput setaf 2; echo "Backup of /etc/hosts created."; tput sgr0
else
    tput setaf 1; echo "Failed to create backup of /etc/hosts."; tput sgr0
    exit 1
fi

# Verify creation of the temporary hosts file
if [ ! -f $TMP_HOSTS ]; then
    tput setaf 1; echo "Temporary hosts file not found after backup creation."; tput sgr0
    exit 1
fi

# Add entries to /etc/hosts
tput setaf 2; echo "Adding entries to /etc/hosts..."; tput sgr0
TOTAL_LINES=$(wc -l < "$WORDLIST")
CURRENT_LINE=0

while IFS= read -r WORD; do
    sudo sh -c "echo '$IP $WORD.$DOMAIN' >> /etc/hosts"
    ((CURRENT_LINE++))
    PERCENTAGE=$((100 * CURRENT_LINE / TOTAL_LINES))
    echo -ne "Progress: $PERCENTAGE% ($CURRENT_LINE/$TOTAL_LINES)\\r"
done < "$WORDLIST"
echo

# Check for 302 responses
tput setaf 4; echo "Checking for 302 responses..."; tput sgr0
TOTAL_LINES=$(wc -l < "$WORDLIST")
CURRENT_LINE=0

while IFS= read -r WORD; do
    URL="http://$WORD.$DOMAIN"
    RESPONSE=$(curl -o /dev/null -s -w "%{http_code}" "$URL")
    ((CURRENT_LINE++))
    PERCENTAGE=$((100 * CURRENT_LINE / TOTAL_LINES))
    
    if [ "$RESPONSE" -eq 302 ]; then
        tput setaf 2; echo "302 Found: $URL"; tput sgr0
    fi

    if [ "$VERBOSE" == "-v" ]; then
        tput setaf 1; echo "Response Code $RESPONSE: $URL"; tput sgr0
    else
        if [ "$RESPONSE" -eq 302 ]; then
            tput setaf 2; echo "302 Found: $URL"; tput sgr0
        fi
        echo -ne "Progress: $PERCENTAGE% ($CURRENT_LINE/$TOTAL_LINES)\\r"
    fi
done < "$WORDLIST"

# Restore original /etc/hosts
cleanup

tput setaf 5; echo "HostHunter complete!"; tput sgr0
