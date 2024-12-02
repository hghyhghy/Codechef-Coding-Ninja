// subarray count

const main=(array,k)=> {

    let n=array.length
    let count = 0

    for (let i=0 ; i<n ; i++){

        let current =0

        for (let j=i ; j<n ; j++){

            current += array[j]

            if (current == k){

                count ++
            }
        }
    }

    return count
}

const arr = [3, 1, 2, 4];
const K = 6;

console.log(main(arr,K))