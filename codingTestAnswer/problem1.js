function solution(s) {
    let resultArray = [];
    let resultStr = '';
    let result = s;
    for (let i = 1; i < s.length; i++) {
        resultStr = '';
        let n = 0;
        let count = 1;
        for (let k = i; k < s.length; k = k + i) {
            if(k > s.length){
                k = s.length - 1;
            }
            if (s.substr(n, i) == s.substr(k, i)) {
                count++
            } else {
                if(count != 1 && count != 0){
                    resultStr = resultStr + count + s.substr(n,i);
                }else{
                    resultStr = resultStr + s.substr(n,i);
                }
                count = 1;
                n = k;
            }
        }
        if(count != 1 && count != 0){
            resultStr = resultStr + count + s.substr(n,i);
        }else{
            resultStr = resultStr + s.substr(n,i);
        }
        
        if(result.length > resultStr.length){
            result = resultStr;
        }
    }
    return result.length;
}
