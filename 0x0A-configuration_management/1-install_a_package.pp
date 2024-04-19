# Using Puppet, install flask from pip3.
class { 'python::pip': }

package { 'Flask':
  ensure => latest,
  provider => 'pip3',
  require => Class['python::pip'],
  version => '2.1.0',
}
