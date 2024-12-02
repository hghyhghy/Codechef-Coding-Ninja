
//find longest substring with  k char

const main = (string,k) => {

    let n = string.length
    let maximum =-Infinity

    for (let i= 0 ; i <n ; i ++){

        let seen =new Set()

        for (let j = i ; j < n ; j++){

            seen.add(string[j])


            if  (seen.size > k){

                break
            }

            maximum=Math.max(maximum,j-i+1)
        }

    }

    return maximum

}
const s = "eceba";
const k = 2;
console.log(main(s, k));