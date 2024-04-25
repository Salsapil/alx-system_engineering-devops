# configuring server with Puppet!
package { 'nginx':
  ensure => installed,
}
nginx::resource::server { 'myserver':
  listen_port => 80,
  server_name => 'localhost',
}
