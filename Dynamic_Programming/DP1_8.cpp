// BOJ 2579
#include <iostream>
using namespace std;

int main() {
	int n;
	int arr[302];
	int dp[302];

	cin >> n;

	arr[0] = 0;
	arr[1] = 0;
	dp[0] = 0;
	dp[1] = 0;

	for (int i = 2; i < n + 2; i++) {
		cin >> arr[i];
		dp[i] = 0;
	}
  
	dp[2] = arr[2];
  
	for (int i = 3; i < n + 2; i++) {
		dp[i] = ((dp[i - 3] + arr[i - 1] + arr[i] > dp[i - 2] + arr[i]) ? dp[i - 3] + arr[i - 1] + arr[i] : dp[i - 2] + arr[i]);
	}
	cout << dp[n + 1] << endl;
}
