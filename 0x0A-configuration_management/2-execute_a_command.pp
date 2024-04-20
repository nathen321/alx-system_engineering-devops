#kill it with fire

exec { 'killmenow':
  command => '/usr/bin/pkill killmenow'
}
