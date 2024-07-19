// https://leetcode.com/problems/plus-one/description/

// You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

// Increment the large integer by one and return the resulting array of digits.

// given a integer as an array add 1 and return updated array
// 1,2,3 => 1,2,4
// 9 => 1,0

function plusOne(arr) {
    let joined = arr.join('')
    console.log(joined)
    let changeInt = parseInt(joined)
    console.log(changeInt)
    let add = changeInt +  1
    console.log(add)
    let changeStr = add.toString()
    console.log(changeStr)
    let spliting = changeStr.split('')
    console.log(spliting)
    let change01 = parseInt(arr.join(''))
    let change02 = change01 + 1
    let change03 = change02.toString().split('')
    console.log(change03)
    return change03
}

// plusOne([1,2,3])
// plusOne([9])
plusOne([6,1,4,5,3,9,0,1,9,5,1,8,6,7,0,5,5,4,3])