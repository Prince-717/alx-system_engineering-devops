exec { 'kill_killmenow_process':
  command     => 'pkill killmenow',
  onlyif      => 'pgrep killmenow',
  path        => '/usr/bin:/bin:/usr/sbin:/sbin', # Set the path to find the commands
  refreshonly => true,
}

