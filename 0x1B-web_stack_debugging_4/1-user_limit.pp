# puppet manifest to edit /etc/security limits.conf
exec { 'fix hard nofile limit':
  command => 'sed -i \'s/^holberton hard nofile.*/holberton hard nofile 65535/g\' /etc/security/limits.conf',
  path    => '/bin/',
}

exec { 'fix soft nofile limit':
  command => 'sed -i \'s/^holberton soft nofile.*/holberton soft nofile 65535/g\' /etc/security/limits.conf',
  path    => '/bin/',
}
