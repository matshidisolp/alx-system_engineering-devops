# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Ensure the Nginx configuration file includes the redirect rule
file_line { 'nginx_redirect_rule':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  after  => 'listen 80 default_server;',
}

# Create index.html file with content
file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

# Ensure Nginx service is running and restarts when configuration changes
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => [
    Package['nginx'],
    File_line['nginx_redirect_rule'],
    File['/var/www/html/index.html'],
  ],
}
