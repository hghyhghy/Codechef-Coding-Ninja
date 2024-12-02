
//binary search

const main = (array,target) => {

    let left =0
    let right = array.length -1

    while ( left <= right){

        let mid = Math.floor((left+right)/2)

        if (array[mid] === target){

            return mid
        }

        if (array[mid] < target){

            left =mid +1
        }
        else{

            right =mid-1
        }




    }

    return  -1
}

const arr = [1, 2, 3, 5, 7, 8, 10];
console.log(main(arr, 8));