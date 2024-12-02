

//common element

const main=(a1,a2,a3) => {

    let i=0,j=0,k=0
    let r=[]

    while ( i<a1.length && j<a2.length && k<a3.length){

        if (a1[i] === a2[j] && a2[j] === a3[k]){

            r.push(a1[i])

        }

        i ++;
        j ++;
        k ++;

        else if (a1[i]<a2[j]){

            i ++
        }

        else if (a2[j]<a3[k]){

            j ++

        }

        else{

            k ++
        }
    }

    return r
}

const A = [2, 3, 4, 7];
const B = [0, 0, 3, 5];
const C = [1, 3, 8, 9];

console.log(main(A, B, C));