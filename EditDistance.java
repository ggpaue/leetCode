/**
 * 
 * @author GGPAUE
 * 
 * Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

 * You have the following 3 operations permitted on a word:

 * a) Insert a character
 * b) Delete a character
 * c) Replace a character
 * 
 */


public class Solution {
	public static int[][] record;
	public int minDistance(String word1, String word2) {
		if(word1.equals(word2)) return 0;
		record = new int[word1.length()][word2.length()];
		for(int i = 0; i < word1.length(); i++) {
			for(int j = 0; j < word2.length(); j++) {
				record[i][j] = -1;
			}
		}
		return dist(word1, word2, word1.length() - 1, word2.length() - 1);
	}
	
	public static int dist(String word1, String word2, int i, int j) {
		if(i < 0 && j < 0) {
			return 0;
		} else if(i < 0 && j >= 0) {
			return j + 1;
		} else if(j < 0 && i >= 0) {
			return i + 1;
		} else {
			if(record[i][j] != -1) return record[i][j];
			String w1 = word1.substring(0, i + 1);
			String w2 = word2.substring(0, j + 1);
			if(w1.equals(w2)) {
				record[i][j] = 0;
				return 0;
			}
			if(w1.contains(w2) || w2.contains(w1)){
				record[i][j] = Math.abs(i - j);
				return Math.abs(i - j);
			}
			if(word1.charAt(i) == word2.charAt(j)) {
				int result = dist(word1, word2, i - 1, j - 1);
				record[i][j] = result;
				return result;
			} else {
				int min = Integer.MAX_VALUE;
				min = Math.min(dist(word1, word2, i - 1, j), dist(word1, word2, i, j - 1));
				min = Math.min(dist(word1, word2, i - 1, j - 1), min);
				min = min + 1;
				record[i][j] = min;
				return min;
			}
		}
	}
	
	

}
