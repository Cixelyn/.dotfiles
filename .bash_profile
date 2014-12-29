# Source local files
if [ -f ~/.bash_profile.local ]; then
  source ~/.bash_profile.local
fi

# color definitions
D=$'\e[37;40m'
PINK=$'\e[35;40m'
GREEN=$'\e[32;40m'
ORANGE=$'\e[33;40m'
RED=$'\e[31;40m'
CYAN=$'\e[36;40m'

if hash vcprompt 2>/dev/null; then
  export PS1='\[${PINK}\]\u\[${D}\]: \[${GREEN}\]\w$(vcprompt -f " [\[\033[36;40m\]%n:%b\[\033[31;40m\]%u%m\[\033[32;40m\]]")\[${D}\] \$ '
else
  export PS1='\[${PINK}\]\u\[${D}\]: \[${GREEN}\]\w\[${D}\] \$ '
fi

# set up pyenv + rbenv if they exist
export RBENV_ROOT=/usr/local/var/rbenv
if which rbenv > /dev/null; then eval "$(rbenv init -)"; fi
if which pyenv > /dev/null; then eval "$(pyenv init -)"; fi
export PYENV_ROOT=/usr/local/opt/pyenv

# set up z.sh
. ~/.dotfiles/z.sh
