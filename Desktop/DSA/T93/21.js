
//pair with given sum

const main=(array,target) =>{

    let n = array.length
    let count  = 0

    for (let i = 0;i < n ; i++){

         for (let j= i+1;j <n; j ++){

             if (array[i]+array[j] === target) {

                 count ++
             }
         }
    }

    return count
}

const arr = [1, 2, 3, 4, 3];
const Sum = 6;

console.log(main(arr,Sum))