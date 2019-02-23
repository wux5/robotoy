#!/usr/bin/env bash

# check color support
colors=$(tput colors)
if (($colors >= 8)); then
    red='\033[0;31m'
    nocolor='\033[00m'
else
  red=
  nocolor=
fi

NAME=`basename ${BASH_SOURCE[0]}`
DESCRIPTION="Watches for filesystem changes in given path and rsync with remote ssh path"

# Define help function
function help(){
    if [[ -z "$1" ]]; then echo "${NAME}: ${DESCRIPTION}"; else echo ${NAME}: $1; fi
    # echo "${NAME} - ${DESCRIPTION}";
    echo "Usage example: ${NAME} -l value -r value -e";
    echo "Options:";
    echo "  -l: LOCAL_PATH. Required. 'Example: /Users/me/folder/'";
    echo "  -r: REMOTE_SSH_PATH. Required. Example: 'user@ssh.server.address:/remote/server/path'";
    echo "  -d: WATCH_DELAY. Optional. Example: '2'";
    exit 1;
}

while getopts ":l:r:d:h" optname
do
    case "$optname" in
      "h")
        help
        ;;
      "l")
        LOCAL_PATH=$OPTARG
        ;;
      "r")
        REMOTE_SSH_PATH=$OPTARG
        ;;
      "d")
        DELAY=$OPTARG
        ;;
      "?")
        help "Invalid option: -$OPTARG"
        ;;
      ":")
        help "Option -$OPTARG requires an argument."
        ;;
      *)
        help "Unknown error while processing options"
        ;;
    esac
done

shift $((OPTIND-1))

# Check required arguments
if [[ -z "$LOCAL_PATH" ]]; then help "Option -l is required"; fi
if [[ -z "$REMOTE_SSH_PATH" ]]; then help "Option -r is required"; fi
if [[ -z "$DELAY" ]]; then DELAY=1; fi
echo LOCAL_PATH=\'$LOCAL_PATH\' REMOTE_SSH_PATH=\'$REMOTE_SSH_PATH\' DELAY=\'$DELAY\'

# Perform initial complete sync
read -n1 -r -p "Press any key to continue (or abort with Ctrl-C)... " key
echo ""
echo -en "${green}"`date` "${nocolor}"". Synchronizing... "
rsync --filter=':- .gitignore' -rvza --progress --force \
       ${LOCAL_PATH} ${REMOTE_SSH_PATH}
echo -e "${green}""Done.""${nocolor}"

fswatch -0 -r -l ${DELAY} -e '\.tmp_files' -e'\.idea' -e'\.git' -e '.*___' -o '\.py|\.wav' . | while read -d "" event
  do
     echo $event > .tmp_files
     echo -en "${green}"`date` "${nocolor}'$event' changed. Synchronizing... "
     rsync --filter=':- .gitignore' -rvza -q --force \
       --include-from=.tmp_files \
       ${LOCAL_PATH} ${REMOTE_SSH_PATH}
     echo -e "${green}""Done.""${nocolor}"
     rm -rf .tmp_files
  done
