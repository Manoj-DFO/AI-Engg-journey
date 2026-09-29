let age = 10
const name = 'manoj'
let n = 12345;
let count = 0
let sum = 0
let rev = 0

console.log(age)
console.log(name)

if (age > 18){
    console.log('eligible to vote')
} else {
    console.log('minor')
}


for (let i = 0; i <= 10 ; i++){
    sum = sum + i
}
console.log(sum)

while (n > 0){
    let a = n % 10
    rev = rev * 10 + a
    n = Math.floor(n / 10)
    count += 1
}
console.log(rev)
console.log(count)


function evenorodd(num){
    if(num % 2 == 0){
        return 'Even'
    } else {
        return 'Odd'
    }
}

console.log(evenorodd(13))

//ARROW FUNCTION
const evenorodd1 = (num) => {
    if (num % 2 == 0) {
        return 'Even';
    } else {
        return 'Odd';
    }
};

console.log(evenorodd1(14));

const evenorodd2 = num => num % 2 === 0 ? 'Even' : 'Odd';

console.log(evenorodd(99));

str = 'manoj'

let rev1 = ''
for (i = str.length - 1 ; i >= 0; i--){
   rev1 += str[i]
}
console.log(rev1)

let max = 0;
let numbers = [10, 45, 23, 89, 12];

for (i = 0; i < numbers.length; i++){
    if (numbers[i] > max){
        max = numbers[i]
    }
}
console.log(max)

let max1 = 0
let rev3 = ''
for (i = 0; i < numbers.length; i++){
    if (numbers[i] > max1){
        max1 = numbers[i]
        rev3 = String(numbers[i]) + rev3
    }
}
console.log(rev3)

let numbers1 = [10, 15, 20, 25, 30];

//map
let result1 = numbers.map(num => num * 2);
console.log(result1);

//filter
let result2 = numbers1.filter(num => num > 20);
console.log(result2);

//reduce
let result3 = numbers1.reduce((sum, num) => sum + num, 0);
console.log(result3);

//find
let result4 = numbers1.find(num => num > 12);
console.log(result4);

//some
let result5 = numbers1.some(num => num > 50);
console.log(result5);

//every
let result6 = numbers1.every(num => num > 0);
console.log(result6);