#include <string>
#include <vector>
#include <iostream>
#include <unordered_map>
#include <cmath>
using namespace std;

int answer = 0;
vector<string> friends = {"A", "C", "F", "J", "M", "N", "R", "T"}; //친구들 배열 생성
vector<int> visited(friends.size());                               //방문 배열 생성(A~T : 0~7)
unordered_map<char, int> um;                                       //맵 생성(A:0, C:1, ~ , T:7), 친구들 배열과 방문 배열을 이어주기 위함

void dfs(int n, vector<string> data, int cnt, string path)
{
    for (int i = 0; i < data.size(); i++) // for문으로 친구들 처음부터 끝까지 돌기
    {
        string d = data[i];
        if (visited[um[d[0]]] == 1 && visited[um[d[2]]] == 1)
        {
            //친구1과 친구2가 visited(친구 각각 더해줬는지, 안더해줬는지 배열)에 모두 존재한다면, 조건에 맞는지를 파악할 수 있다.
            int space = d[4] - '0';
            int tmpSpace = path.find(d[0]) - path.find(d[2]);
            if (d[3] == '=')
            { // data(조건 배열)에서 하나씩 조건에 맞는지 찾아낸다.
                if (abs(tmpSpace) - 1 != space)
                {
                    return;
                }
            }
            else if (d[3] == '>')
            { //친구1과 친구2가 전부 존재함으로, 두 명의 간격을 알아 낸 후, 조건에 맞는 간격이 아니라면 return 해줌으로써 백트래킹을 한다.
                if (abs(tmpSpace) - 1 <= space)
                {
                    return;
                }
            }
            else
            {
                if (abs(tmpSpace) - 1 >= space)
                {
                    return;
                }
            }
        }
    }

    if (cnt == friends.size())
    { //계속 조건파악에도 return되지 않고, cnt 횟수가 8명까지 왔으면, 이것이 정답이므로 answer + 1을 해줌
        answer += 1;
        return;
    }

    for (int i = 0; i < friends.size(); i++) //방문하지 않았다면 path(순서)에 친구 한명을 더해줌
    {
        if (visited[i] == 0)
        {
            visited[i] = 1;
            string tmpPath = path + friends[i];
            dfs(n, data, cnt + 1, tmpPath);
            visited[i] = 0;
        }
    }
}

int solution(int n, vector<string> data)
{
    um['A'] = 0;
    um['C'] = 1;
    um['F'] = 2;
    um['J'] = 3;
    um['M'] = 4;
    um['N'] = 5;
    um['R'] = 6;
    um['T'] = 7;

    answer = 0;
    dfs(n, data, 0, "");

    return answer;
}