function Bear(opts){
  if(!(this instanceof Bear)) return new Bear(opts)
  opts = opts || {}
  this.type = opts.type || 'bear'
  console.log(opts)
}

Bear.prototype.growl = function(){
  console.log('grr')
  return this
}

Bear.prototype.walk = function(){
  console.log('wlk')
  return this
}

Bear.prototype.eat = function(){
  console.log('eats me')
  return this
}

var grizzly = new Bear({
  type: 'grizzly',
  say: 'grr'
})

grizzly.growl().walk().eat()
