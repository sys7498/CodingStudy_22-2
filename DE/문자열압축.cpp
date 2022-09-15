#include <string>
#include <vector>
#include <algorithm> //min 사용

using namespace std;

int solution(string s)
{
    int answer = s.length(); // 입력받은 문자열의 길이를 최초값으로 설정
    for (int i = 1; i <= s.length() / 2; ++i)
    {                         //압축할 단위의 길이를 i로 설정, 문자열의 절반까지만 반복하면 됨.
        int position = 0;     // 0번부터 위치 설정
        int len = s.length(); //단위마다 압축했을 때 작아지는 길이를 빼줌으로써 최종 압축 길이를 구함

        for (;;)
        {                                        //무한 루프
            string unit = s.substr(position, i); //압축이 되는 문자를 unit에 가져옴, substr 두번째인자는 i길이만큼 반환
            position += i;                       //동일한 문자가 존재하는지 가져옴

            if (position >= s.length())
                break; // position이 입력된 문자열 끝에 이르면 break

            int count = 0; //뒤에 연속된 문자를 세는 변수
            for (;;)
            {
                if (unit.compare(s.substr(position, i)) == 0)
                {                  // 0이면 같은 문자
                    ++count;       // count를 하나 센다.
                    position += i; // 그 뒤에도 연속된 문자가 있을 수 있으므로 반복한다.
                }
                else
                { //같지 않을 경우 다음 기준이 되는 문자를 가져와서 이 과정을 반복한다.
                    break;
                }
            }
            if (count > 0)
            {                     // 0 이상이면 압축된 것이 있다는 것
                len -= i * count; //반복된 횟수 만큼 빼준다.(반복된 단위 개수 * 단위 길이)

                if (count < 9)
                    len += 1; //연속된 숫자를 세기 위함
                else if (count < 99)
                    len += 2;
                else if (count < 999)
                    len += 3;
                else
                    len += 4;
            }
        }
        answer = min(answer, len);
    }
    return answer;
}