#user-defined(levi):
alias scanwifi='sudo iwlist scan > /dev/null && nmcli dev wifi'
alias showip="nmcli dev show | grep 'DEVICE\|TYPE\|HWADDR\|STATE\|CONNECTION\|ADDRESS\|GATEWAY\|DNS' -m 8"
#nmcli dev wifi won't show whole wifi list until you scan it first
export CDPATH='.:~'
#'.'means search current directroies first, 
#'~'means serach ~ directroies secondly~
alias syslog='sudo cat /var/log/syslog'
