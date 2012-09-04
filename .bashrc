#Custom PS1 setting
case "$TERM" in
linux|xterm*|rxvt*|screen*)
    PS1="\[\033[0;33m\]Exit status: \$?\[\033[0m\]\n"'${debian_chroot:+($debian_chroot)}\[\033[0;34m\]\u\[\033[0m\]@\[\033[0;32m\]\h\[\033[0m\]:\[\033[0;33m\]\w
\[\033[0;39m\]\$\[\033[0m\] '
    ;;
*)
    PS1="Exit status: \$?\n"'${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
    ;;
esac

#MOST like colored man pages
export LESS_TERMCAP_mb=$'\E[1;34m'
export LESS_TERMCAP_md=$'\E[1;34m'
export LESS_TERMCAP_me=$'\E[m'
export LESS_TERMCAP_us=$'\E[1;32m'
export LESS_TERMCAP_ue=$'\E[m'
export LESS_TERMCAP_so=$'\E[1;33;42m'
export LESS_TERMCAP_se=$'\E[m'


# 忽略重复的命令
export HISTCONTROL=ignoredups
# 忽略由冒号分割的这些命令
export HISTIGNORE="[   ]*:&:bg:fg:exit"
# 设置保存历史命令的文件大小
export HISTFILESIZE=1000000000
# 保存历史命令条数
export HISTSIZE=1000000

# 以追加的方式记录命令历史
shopt -s histappend

# 每次执行完命令，更新历史记录
PROMPT_COMMAND="history -a; $PROMPT_COMMAND"

if [ -d "$HOME/myHomeConfs/bin" ] ; then
    export PATH="$HOME/myHomeConfs/bin:$PATH"
fi

if [ -d "$HOME/work/devel/android-sdk-linux_86/platform-tools" ] ; then
    export PATH="$HOME/work/devel/android-sdk-linux_86/platform-tools:$PATH"
fi
