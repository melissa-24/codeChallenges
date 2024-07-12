// https://www.codewars.com/kata/5c3433a4d828182e420f4197

const ultimateReverse = s => {
    //   Get each index of the arrays origional length
    //   Concat the strings
    //   Reverse the string
    //   Re divide the string to the index
    var arrIndexLength = []
    var concatString = ''
    var newConcatString = ''
    var newArr = []
    var indexOne = 0
    var indexTwo = 0
    //   finding the length of each index of the origional array adding it to a new array
    //   taking each element of the array and combining it into a single string
    for (var i = 0; i < s.length; i++) {
        arrIndexLength.push(s[i].length)
        concatString += s[i]
        console.log(concatString)
    }
    console.log(arrIndexLength)
    console.log(concatString)

    // putting it back into an array , reversingit, and back to a string
    newConcatString = concatString.split('').reverse().join('');
    console.log(newConcatString)

    //   taking the string and putting it back into an array but reverse
    for (var i = 0; i < arrIndexLength.length; i++) {
        console.log('value of i', arrIndexLength[i])
        indexTwo = indexOne + arrIndexLength[i]
        var temp = newConcatString.slice(indexOne, indexTwo)
        newArr.push(temp)
        indexOne += arrIndexLength[i]
        console.log('temp', temp, 'newArr', newArr, 'indexOne', indexOne, 'indexTwo', indexTwo)
    }
    console.log(newArr)
    return newArr
};