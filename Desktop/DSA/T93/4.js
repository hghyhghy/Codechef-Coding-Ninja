

const main=(array)=> {

    let new_array= array.map(x=> x**2)

    new_array.sort((a,b)=>a-b)

    return new_array
}


const arr = [-6, -3, 2, 1, 5];
console.log(main(arr))
