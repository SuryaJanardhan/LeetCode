function processStr(s: string): string {
    let stack: string[] = []
    for( let i of s){
        if (i === '*'){
            if (stack){
                stack.pop()
            }
        }
        else if(i === '#'){
            stack.push(...stack);        }
        else if( i === '%'){
            stack.reverse()
        }
        else{
            stack.push(i)
        }
    }

    return stack.join("");
};