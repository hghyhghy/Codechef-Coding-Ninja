
// move zero

const  main =(array) =>{

    let n=array.length
    let zero = 0

    for (let i=0 ; i< n ; i++){


        if (array[i ] !== 0){

            [array[zero],array[i]]=[array[i],array[i]]

             zero ++
        }

    }

    return array


}

const arr = [0, 1, -2, 3, 4, 0, 5, -27, 9, 0];
console.log(main(arr))