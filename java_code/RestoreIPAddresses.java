/**
 * 
 * Given a string containing only digits, restore it by returning all possible valid IP address combinations.
 *
 * For example:
 * Given "25525511135",
 *
 * return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
 *  
 */

import java.util.*;
public class Solution {
	public ArrayList<String> restoreIpAddresses(String s) {
		ArrayList<String> result = restoreIpAddresses(s, 4);
		if(result == null) result = new ArrayList<String>();
		return result;	
	}
	
	public ArrayList<String> restoreIpAddresses(String s, int k) {
		assert(k >= 1 && k <= 4);
		if(s == null || s.length() < k || s.length() > 3 * k) return null;
		ArrayList<String> result = new ArrayList<String>();
		
		for(int i = 0; i < Math.min(s.length(), 3); i++) {
			String num = s.substring(0, i + 1);
			if((i == 0 || num.charAt(0) > '0') && Integer.parseInt(num) <= 255) {
				if(k == 1) {
					if(i == s.length() - 1) {
						result.add(num);
					}
				} else {
					ArrayList<String> remain = restoreIpAddresses(s.substring(i + 1), k - 1);
					if(remain != null) {
						for(String r : remain) {
							String temp = num + '.' + r;
							result.add(temp);
						}
					}
				}
			} else {
				break;
			}
		}
		return result;
	}

}
