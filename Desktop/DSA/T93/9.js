
//subarray divisible

const main=(array,k) => {

    let n= array.length
    let count =0

    for (let i=0;i<n;i++){

        let curr =0

        for (let j=i;j<n;j++){

            curr += array[j]


            if ( curr %k ===0){

                count ++
            }
        }
    }

    return count
}


const arr = [2, 3, 4, 6];
const k = 3;

console.log(main(arr,k))