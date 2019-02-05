/**
 * 
 * Given an array of strings, return all groups of strings that are anagrams.

 * Note: All inputs will be in lower-case.
 * 
 */


import java.util.*;
public class Solution {
	public ArrayList<String> anagrams(String[] strs) {
		int len = strs.length;
		ArrayList<String> result = new ArrayList<String>();
		if(len <= 1) return result;
		
		Map<String, Integer> map = new HashMap<String, Integer>();
		
		String[] record = new String[len];
		
		for(int i = 0; i < len; i++) {
			String h = hash(strs[i]);
			if(map.get(h) != null) {
				map.put(h, map.get(h) + 1);
			} else {
				map.put(h, 1);
			}
			
			record[i] = h;
		}
		
		for(int i = 0; i < len; i++) {
			if(map.get(record[i]) > 1) {
				result.add(strs[i]);
			}
		}
		
		return result;
	}
	
	public static String hash(String str) {
		StringBuilder result = new StringBuilder();
		char[] arr = str.toCharArray();
		if(arr.length == 0) return "";
		Arrays.sort(arr);
		String h = new String(arr);
		result.append(h.hashCode());
		return result.toString();
	}

}
