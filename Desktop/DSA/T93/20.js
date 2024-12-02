
//first repeating  character

const main=(array)=> {

    const freq={}

    for (let num of  array){

        if (freq[num]) {

            freq[num] ++
        }
        else{

            freq[num] = 1
        }
    }

    const r=[]
    for (let num in freq){

        if (freq[num ] === 1){

            r.push(parseInt(num))
        }
    }

    return r
}

const arr = [4, 7, 3, 2, 7, 2];
console.log(main(arr));

