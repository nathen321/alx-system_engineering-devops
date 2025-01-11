# Install an especific version of flask

package { 'flask':
  name     => 'Flask'
  ensure   => '2.1.0',
  provider => 'pip3',
}
