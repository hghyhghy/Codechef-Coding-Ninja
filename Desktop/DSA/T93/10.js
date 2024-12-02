
//move zero to end

const main=(array) => {

    let zero=[]
    let non_zero=[]

    for(let num of array){

        if (num === 0){

            zero.push(num)
        }

        else {

            non_zero.push(num)
        }
    }

    return non_zero.concat(zero)
}

const arr = [0, 1, -2, 3, 4, 0, 5, -27, 9, 0];
console.log(main(arr))