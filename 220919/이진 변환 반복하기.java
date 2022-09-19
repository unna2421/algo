class Solution {
    public int[] solution(String s) {
        int[] answer = new int[2];
        int tryCount = 0;
        int zeroCount = 0;
        while (!s.equals("1")) {
            tryCount ++;
            String temp = s.replaceAll("0", "");
            int zeroTemp = 0;
            zeroTemp = s.length() - temp.length();
            zeroCount += zeroTemp;

            s = Integer.toBinaryString(temp.length());
        }
        answer[0] = tryCount;
        answer[1] = zeroCount;
        
        return answer;
    }
}