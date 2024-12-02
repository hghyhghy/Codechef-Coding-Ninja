
//function

const main=(array,x)=> {

    let freq={}

    for (let num of array){

        if (freq[num] !== undefined){

            freq[num] +=1

        }

        else {

            freq[num] = 1
        }
    }

    return freq[x] !== undefined ?  freq[x] : 0
}

const arr = [2, 1, 3, 5, 6, 0, 9, 0];
const x = 0;

console.log(main(arr,x))