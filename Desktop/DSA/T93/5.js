

//buy and sell stock

const main = (array)=> {

    let maximum=0
    let minimum=Infinity

    for (let  num  of array){

        if (num<minimum){

            minimum = num

        }

        let profit = num - minimum

        if (profit > maximum){

            maximum = profit

        }
    }

    return maximum

}

const prices = [7, 1, 5, 3, 6, 4];
console.log(main(prices))