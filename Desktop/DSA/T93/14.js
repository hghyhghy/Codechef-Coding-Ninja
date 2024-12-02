
//remove duplicates

const  main = (string) => {

    let seen= new Set()
    let r= []

    for (let char of string){

        if  (!seen.has(char)){

            seen.add(char)

            r.push(char)
        }
    }

    return r.join("")
}

const str = "abcadeecfb";
console.log(main(str));