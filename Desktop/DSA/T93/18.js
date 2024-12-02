
//next smaller element

const  main=(array) => {

    let n = array.length
    let dp=Array(n).fill(-1)

    for (let i=0 ; i<n ; i++){

        for(let j=i+1;j<n;j++){

            if (array[j]<array[i]){

                dp[i]=array[j]
                break
            }
        }
    }

    return dp
}

const arr = [4, 5, 2, 10, 8];
console.log(main(arr));