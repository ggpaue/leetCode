/**
 * 
 * Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
 * 
 * For example, given
 * s = "leetcode",
 * dict = ["leet", "code"].
 * 
 * Return true because "leetcode" can be segmented as "leet code".
 * 
 */

import java.util.*;
public class Solution {
	public boolean wordBreak(String s, Set<String> dict) {
		ArrayList<Integer> list = new ArrayList<Integer>();
		for(int i = s.length() - 1; i >= 0; i--) {
			String sub = s.substring(i);
			if(dict.contains(sub)) {
				list.add(i);
			} else {
				for(Integer index : list) {
					sub = s.substring(i, index);
					if(dict.contains(sub)) {
						list.add(i);
						break;
					}
				}
			}
		}
		if(list.isEmpty()) {
			return false;
		} else {
			Integer index = list.get(list.size() - 1);
			return index == 0;
		}
	}

}
