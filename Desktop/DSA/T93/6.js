
//maximum length

const main=(array) => {

    let n=array.length
    let maximum =  0

    for (let i =0 ; i< n; i++){

        let current = 0

        for (let j=i ; j<n ; j ++){

            current += array[j]

            if (current === 0){

                maximum = Math.max(maximum,j-i+1)
            }
        }
    }

    return maximum


}

const arr = [1, -1, 3, 2, -2, -3, 3];
console.log(main(arr))