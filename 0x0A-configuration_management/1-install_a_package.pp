# Using Puppet, install flask from pip3.
class { 'python':
  version => '3.8.10',
}

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
