
//bubble sort in java

const  bubble =(array) => {

    let n=array.length

    for (let i=0 ; i<n ; i++){

        for (let j=0;j<n-i-1;j++){

            if (array[j]>array[j+1]){

                [array[j],array[j+1]]=[array[j+1],array[j]]

            }
        }
    }

    return array

}

const main=(array,k) => {

    let temp= bubble(array)

    return temp[k-1]
}

const arr = [12, 3, 5, 7, 19];
console.log(main(arr,2))