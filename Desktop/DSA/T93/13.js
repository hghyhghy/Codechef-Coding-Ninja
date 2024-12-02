
//peak element

const main=(array)=> {

    let n= array.length

    if (n===0){

        return 0
    }

    if (array[0]>array[1]){

        return  0
    }

    if (array[n-1]>array[n-2]){

        return  array[n-1]
    }

    for (let i=1;i<n-1;i++){

        if( array[i-1]<array[i] && array[i]>array[i+1]){

            return  i
        }
    }

    return  -1


}


const arr = [4, 6, 3, 2];
console.log(main(arr));
