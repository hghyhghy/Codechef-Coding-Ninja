
//bubble sort


const main=(array) => {

    let n=array.length

    for (let i=0;i <n ;i ++){

        for (let j=0;j < n-i-1 ;j ++){

            if  (array[j]>array[j+1]){

                [array[j],array[j+1]]=[array[j+1],array[j]]
            }
        }
    }

    return array
}

const arr = [6, 8, 9, 2, 3];
console.log(main(arr));