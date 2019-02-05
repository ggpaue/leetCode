/*
* Given a string s, partition s such that every substring of the partition is a palindrome.

* Return all possible palindrome partitioning of s.

* For example, given s = "aab",
* Return

*  [
*  ["aa","b"],
*  ["a","a","b"]
*  ]
*/
import java.util.*;
public class Solution {
	public ArrayList<ArrayList<String>> partition(String s) {
		ArrayList<ArrayList<String>> results = new ArrayList<ArrayList<String>>();
		int length = s.length();
		if(length == 0) return results;
		ArrayList<String> pt = new ArrayList<String>();
		findPartition(s, 0, pt, results);
		return results;
	}
	void findPartition(String s, int start, ArrayList<String> pt, ArrayList<ArrayList<String>> results) {
		if(start >= s.length()) {
			ArrayList<String> copy = new ArrayList<String>();
			for(int j=0; j<pt.size(); j++) {
				copy.add(pt.get(j));
			}
			results.add(copy);
		}
		for (int i = start; i<s.length(); i++) {
			if(isPalindrome(s, start, i)) {
				pt.add(s.substring(start, i+1));
				findPartition(s, i+1, pt, results);
				pt.remove(pt.size() - 1);
			}
		}
	}
	boolean isPalindrome(String s, int begin, int end) {
		while(begin < end) {
			if(s.charAt(begin) != s.charAt(end)) {
				return false;
			}
			begin++;
			end--;
		}
		return true;
	}

}
