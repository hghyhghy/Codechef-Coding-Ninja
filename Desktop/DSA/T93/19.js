

//minimum of k size

const main=(array,k) => {

    let  n= array.length
    let minimum =Infinity

    for (let i=0;i<=n-k;i++){

        let current = 0

        for (let j=0;j<k;j++){

            current += array[i+j]

        }

        if (current < minimum){

            minimum = current
        }
    }

    return minimum
}

const N = 7;
const K = 3;
const ARR = [2, 1, 5, 1, 3, 2, 1];
console.log(main(ARR, K))