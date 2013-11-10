if [ -f ~/.bash_profile.local ]; then
  source ~/.bash_profile.local
fi

# COLOR DEFINITIONS
D=$'\e[37;40m'
PINK=$'\e[35;40m'
GREEN=$'\e[32;40m'
ORANGE=$'\e[33;40m'
RED=$'\e[31;40m'
CYAN=$'\e[36;40m'

if hash vcprompt 2>/dev/null; then
  export PS1='\[${PINK}\]\u\[${D}\]: \[${GREEN}\]\w$(vcprompt -f " [\[\033[36;40m\]%b\[\033[31;40m\]%u%m\[\033[32;40m\]]")\[${D}\] \$ '
else
  export PS1='\[${PINK}\]\u\[${D}\]: \[${GREEN}\]\w\[${D}\] \$ '
fi
