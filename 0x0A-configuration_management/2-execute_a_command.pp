#kill it with fire

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
