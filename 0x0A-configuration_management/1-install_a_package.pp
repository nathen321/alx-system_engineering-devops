# Install an especific version of flask

exec { 'flask':
  command => '/usr/bin/pip3 install Flask'
}
