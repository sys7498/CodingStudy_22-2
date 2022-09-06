function solution(s) {                                                  //솔루션
    let resultStr = '';                                                 //결과스트링 resultStr
    let result = s;                                                     //결과(답)을 s로 초기화 result
    for (let i = 1; i < s.length; i++) {                                //input스트링의 길이만큼 반복
        resultStr = '';                                                 //반복실행마다 초기화
        let n = 0;                                                      //같은 문자가 아닐때의 인덱스 표시해주는 변수 n
        let count = 1;                                                  //같은 문자가 몇번 나왔는지 알려주는 변수 count
        for (let k = i; k < s.length; k = k + i) {                      //input스트링의 길이만큼 반복
            if (k > s.length) {                                         //k가 input스트링의 길이보다 크다면
                k = s.length - 1;                                       //k를 마지막 요소의 인덱스로 초기화
            }
            if (s.substr(n, i) == s.substr(k, i)) {                     //n부터 i까지의 스트링이 k부터 i까지의 스트링과 같다면
                count++                                                 //count를 하나씩 더하기
            } else {                                                    //만약 아닐 경우,
                if (count != 1 && count != 0) {                         //근데 만약 count가 1도아니고 0도 아니라면(0은 있을 수가 없고, 1은 생략하기로 하였기 때문에)
                    resultStr = resultStr + count + s.substr(n, i);     //resultStr을 지금까지의 같은 스트링의 수와 스트링을 붙인 스트링으로 초기화
                } else {                                                //근데 만약 그 경우가 아니라면
                    resultStr = resultStr + s.substr(n, i);             //resultStr을 그냥 기존 resultStr에 지금까지의 스트링을 붙인 스트링으로 초기화
                }
                count = 1;                                              //두 경우를 다 검사한 후 count = 1으로 초기화
                n = k;                                                  //n = k로 초기화
            }
        }
        if (count != 1 && count != 0) {                                 //반복이 끝날때까지 같은 스트링이 나오면 resultStr을 다시 초기화하는 과정을 못하였기 때문에 위의 과정을 한번 더 실행
            resultStr = resultStr + count + s.substr(n, i);             //
        } else {                                                        //
            resultStr = resultStr + s.substr(n, i);                     //
        }

        if (result.length > resultStr.length) {                         //result의 길이와 resultStr의 길이중 더 짧은 것을 
            result = resultStr;                                         //result로 초기화
        }
    }
    return result.length;                                               //결과 리턴
}
