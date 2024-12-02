function minimum(array) {

    if (!array || array.length == 0){

        return array
    }

    let smallest = array[0]

    for (let num of  array){

        if (num < smallest) {

            smallest = num

        }
    }

    return  smallest
}

const arr = [4, 5, 6, 1, 2, 3]
console.log(minimum(arr))