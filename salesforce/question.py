"""
public static List<Integer> predictAnswer(List<Integer> stockData, List<Integer> queries) {
    List<Integer> resQuery = new ArrayList<>();

    /* to show -1 if there is no such stock price */
    for (int i = 0; i < queries.size(); i++) {
        resQuery.add(-1);
    }

    for (int i = 0; i < queries.size(); i++) {
        /* the query index starts from 1 or supposes the first index is 1 */
        int index = (int) (queries.get(i) - 1);
        int value = stockData.get(index).intValue();

        int j = index + 1;
        int k = index - 1;

        while (j < stockData.size() - 1 || k > 1) {

            if (k < 1) {
                if (stockData.get(j).intValue() < value) {
                    resQuery.set(i, j + 1);
                    break;
                }
            }

            else if (j > stockData.size() - 1) {
                if (stockData.get(k).intValue() < value) {
                    resQuery.set(i, k + 1);
                    break;
                }
            }

            else if (stockData.get(k).intValue() < value) {
                resQuery.set(i, k + 1);
                break;
            }

            else if (stockData.get(j).intValue() < value) {
                resQuery.set(i, j + 1);
                break;
            }

            j++;
            k--;
        }
    }
}


using namespace std;

string ltrim(const string &);
string rtrim(const string &);



/*
 * Complete the 'predictAnswer' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY stockData
 *  2. INTEGER_ARRAY queries
 */

void precompute(vector<int>* stockData, vector<int>* result, int dir) {
    stack<int> st;
    int start = (dir == 1 ? 0 : (stockData->size() - 1));
    int end = (dir == 1 ? stockData->size() : -1);
    for (int i = start; i != end; i += dir) {
        if (st.empty()) {
            st.push(i);
        } else {
            while (!st.empty() && stockData->at(st.top()) > stockData->at(i)) {
                result->at(st.top()) = i;
                st.pop();
            }
            st.push(i);
        }
    }
    while (!st.empty()) {
        result->at(st.top()) = -1;
        st.pop();
    }
}

vector<int> predictAnswer(vector<int> stockData, vector<int> queries) {
    vector<int> lowerRight(stockData.size() + 5);
    vector<int> lowerLeft(stockData.size() + 5);
    precompute(&stockData, &lowerRight, 1);
    precompute(&stockData, &lowerLeft, -1);

    for (int i : lowerRight) cout << i << " "; cout << endl;
    for (int i : lowerLeft) cout << i << " "; cout << endl;

    vector<int> ans;
    for (int q : queries) {
        q--; // adjustment to zero-based index
        if (lowerRight[q] == -1 && lowerLeft[q] == -1) {
            ans.push_back(-1);
        } else if (lowerRight[q] == -1) {
            ans.push_back(lowerLeft[q] + 1);
        } else if (lowerLeft[q] == -1) {
            ans.push_back(lowerRight[q] + 1);
        } else {
            int distToLeft = q - lowerLeft[q];
            int distToRight = lowerRight[q] - q;
            if (distToLeft <= distToRight) {
                ans.push_back(lowerLeft[q] + 1);
            } else {
                ans.push_back(lowerRight[q] + 1);
            }
        }
    }
    return ans;
}

int main()
{

    string stockData_count_temp;
    getline(cin, stockData_count_temp);

    int stockData_count = stoi(ltrim(rtrim(stockData_count_temp)));

    vector<int> stockData(stockData_count);

    for (int i = 0; i < stockData_count; i++) {
        string stockData_item_temp;
        getline(cin, stockData_item_temp);

        int stockData_item = stoi(ltrim(rtrim(stockData_item_temp)));

        stockData[i] = stockData_item;
    }

    string queries_count_temp;
    getline(cin, queries_count_temp);

    int queries_count = stoi(ltrim(rtrim(queries_count_temp)));

    vector<int> queries(queries_count);

    for (int i = 0; i < queries_count; i++) {
        string queries_item_temp;
        getline(cin, queries_item_temp);

        int queries_item = stoi(ltrim(rtrim(queries_item_temp)));

        queries[i] = queries_item;
    }

    vector<int> result = predictAnswer(stockData, queries);

    for (int i = 0; i < result.size(); i++) {
        cout << result[i];

        if (i != result.size() - 1) {
            cout << "\n";
        }
    }

    cout << "\n";

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}



"""

def predictAnswer_2(stockData, queries):
    results = []

    for i in range(len(queries)):
        results.append(-1)

    for i in range(len(queries)):
        index = queries[i] - 1
        value = stockData[index]

        j = index + 1
        k = index + 1

        while j < len(stockData) - 1 or k > 1:
            if k < 1:
                if stockData[j] < value:
                    results.insert(i, j + 1)
                    break
            elif j > len(stockData) - 1:
                if stockData[k] < value:
                    results.insert(i, k + 1)
                    break
            elif stockData[k] < value:
                results.insert(i, k + 1)
            elif stockData[j] < value:
                results.insert(i, j + 1)
                break
            j += 1
            k -= 1

    return results


def predictAnswer(stockData, queries):
    lower_right = []
    lower_left = []
    compute(stockData, lower_right, 1)
    compute(stockData, lower_left, -1)

    answer = []
    for q in queries:
        q -= 1
        if lower_right[q] == -1 and lower_left[q] == -1:
            answer.append(-1)
        elif lower_right[q] == -1:
            answer.append(lower_left[q] + 1)
        elif lower_left[q] == -1:
            answer.append(lower_right[q] + 1)
        else:
            dist_to_left = q - lower_left[q]
            dist_to_right = lower_right[q] - q
            if dist_to_left <= dist_to_right:
                answer.append(lower_left[q] + 1)
            else:
                answer.append(lower_right[q] + 1)

    return answer


def compute(stockData, results, dir):
    stack = []
    start = 0 if dir == 1 else len(stockData) - 1
    end = len(stockData) - 1 if dir == 1 else -1
    for i in range(start, end, dir):
        if len(stack) == 0:
            stack.append(i)
        else:
            while len(stack) != 0 and stockData[stack[0]] > stockData[i]:
                results.insert(stack[0], i)
                stack.pop()
            stack.append(i)
    while len(stack) != 0:
        results.insert(stack[0], -1)
        stack.pop()


if __name__ == '__main__':
    stockData = [5, 6, 8, 4, 9, 10, 8, 3, 6, 4]
    queries = [6, 5, 4]

    results = predictAnswer(stockData, queries)
    print(results)