class Solution {
    public String solution(String s) {
        String answer = "";
        String[] strArr = s.toLowerCase().split("");
        boolean space = true;
        for(String str :strArr){
            answer += space ? str.toUpperCase() : str;
            space = str.equals(" ") ? true : false;
        }
        return answer;
    }
}