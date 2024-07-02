#execute a command to kill process with puppet

exec { 'pkill -f killmenow':
  path  => 'usr/bin/:/usr/local/bin/:/bin/',
}
