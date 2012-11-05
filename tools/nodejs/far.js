var boo = function () {};

for(var i in boo.prototype) {
    console.log(i);
}
