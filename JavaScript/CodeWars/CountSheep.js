// https://www.codewars.com/kata/5b077ebdaf15be5c7f000077

// If you can't sleep, just count sheep!!

// Task:
// Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.

// loop through numbers starting at 1 to provided number and add a space and sheep... but possibly no space at the end of sheep...
// always valid and no negative is given

function countSheep(n) {
    result = ''
    // console.log(n, "sheep...")
    for(var i = 1; i <= n; i++) {
        res = i + " sheep..."
        // console.log(i, "sheep...")
        result = result + res
    }
    console.log(result)
    return result
}

countSheep(4)