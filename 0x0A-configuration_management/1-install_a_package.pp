class { 'python::pip': }

package { 'Flask':
  ensure => installed,
  provider => 'pip3',
  require => Class['python::pip'],
  version => '2.1.0',
}
