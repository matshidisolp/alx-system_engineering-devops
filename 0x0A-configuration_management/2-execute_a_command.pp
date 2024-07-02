#execute a command to kill process with puppet

execute { 'pkill -f killmenow':
  path  => 'usr/bin/:/usr/local/bin/:/bin/',
}
