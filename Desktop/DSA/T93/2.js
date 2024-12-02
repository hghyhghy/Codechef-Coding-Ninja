// #maximum product subarray

const main =(array) => {

    let n=array.length
    let maximum = Number.NEGATIVE_INFINITY

    for (let i=0; i<n ;i ++){

        let product = 1

        for (let j = i;j < n;j ++){

            product *= array[j]

            if (product > maximum){

                maximum = product
            }
        }
    }

    return maximum

}

const arr = [2, 3, -2, 4];
console.log(main(arr))