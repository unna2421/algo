class Solution {
    public int solution(int n) {
        int answer = 0;
        int[] arr = new int[n];
        for(int i = 0; i < n; i++) {
            arr[i] = i+1;
        }
        for(int i = 0; i < n; i++) {
            int sum = 0;
            int k = i;
            while(true) {
                sum += arr[k++];
                if(sum >= n) break;
            }
            if(sum == n) answer++;
        }
        return answer;
    }
}