file { '/tmp/school':
  ensure  => file,          # Ensure that the file exists
  mode    => '0744',        # Set the file permissions
  owner   => 'www-data',    # Set the file owner
  group   => 'www-data',    # Set the file group
  content => 'I love Puppet', # Set the file content
}

