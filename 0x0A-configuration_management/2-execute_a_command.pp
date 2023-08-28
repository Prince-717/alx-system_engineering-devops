# Executes a bash command
exec { 'kill':
  command     => 'pkill -f killmenow',
  onlyif      => 'pgrep killmenow',
  path        => ['/usr/bin', '/usr/sbin'] # Set the path to find the commands
  refreshonly => true,
}

