let x = 3
console.log(x)
function sayHi(x) { console.log(4+x) }
sayHi(x)
const y = x + 99760
console.log(y, "hi")

for(let i = 0; i < x; i + 2) { console.log(i) }
for(let i = 0; i < x; i++) { console.log(i) }

let myArr = ["a", "b", "c"]
console.log(myArr)

for(let i = 0; i < x; i++) { console.log(myArr[i]) }
for(let i = 0; i < myArr.length; i++) { console.log(myArr[i]) }

var myObj1 = { key1: "value1" }
var myObj2 = { key1: "value1", key2: "value2" }
console.log(myObj1, myObj2)

let val1 = myObj1.key1
// let val2 = myObj1["key1"]
console.log(val1)