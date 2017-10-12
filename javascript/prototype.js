function Bear(type){
  this.type = type
}
Bear.prototype.growl = function(){
  console.log( 'the ' + this.type + ' bear says grrrr' )
}

function Grizzly(){
  Bear.call(this, 'grizzly')
}
Grizzly.prototype = Object.create(Bear.prototype)



var context = {
  type: 'grizzly_context',
  say: 'varcontext'
}
bear_func = bear_func.bind(context)



var says = bear_func()
console.log(says)

function bear_func(){
  console.log(arguments)
  return 'The ' + this.type + ' bear says ' + this.var1
}
