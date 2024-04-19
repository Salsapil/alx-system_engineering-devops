# Using Puppet, install flask from pip3.
class { 'python::pip': }

package { 'Flask':
  ensure => '2.1.0',
  provider => 'pip3',
}

package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
  require  => Package['Flask'],
}
