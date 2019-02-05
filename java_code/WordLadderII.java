/**
 * 
 * Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start to end, such that:
 *
 * Only one letter can be changed at a time
 * Each intermediate word must exist in the dictionary
 * For example,
 * 
 * Given:
 * start = "hit"
 * end = "cog"
 * dict = ["hot","dot","dog","lot","log"]
 *
 * Return
 *
 *   [
 *     ["hit","hot","dot","dog","cog"],
 *     ["hit","hot","lot","log","cog"]
 *   ]
 * Note:
 * 
 * All words have the same length.
 * All words contain only lowercase alphabetic characters.
 * 
 * 
 */

import java.util.*;

public class Solution {
    public ArrayList<ArrayList<String>> findLadders(String start, String end, HashSet<String> dict) {
        // Start typing your Java solution below
        // DO NOT write main() function
    	HashSet<String> visited = new HashSet<String>();
        LinkedList<ArrayList<String>> resultList = new LinkedList<ArrayList<String>>();
        ArrayList<String> temp = new ArrayList<String>();
        boolean found = false;
        
        temp.add(start);
        resultList.add(temp);
        
        while(!resultList.isEmpty()) {
            for(int i = 0; i < resultList.size(); i++) {
            	ArrayList<String> list = resultList.pollFirst();
            	String from = list.get(list.size() - 1);
            	visited.add(from);
            	char[] array = from.toCharArray();
            	for(int j = 0; j < array.length; j++) {
            		char base = array[j];
            		for(char c = 'a'; c < 'z'; c++) {
            			if(c == base) continue;
            			array[j] = c;
            			String s = new String(array);
            			if(dict.contains(s) && !visited.contains(s)) {
            				if(s.equals(end)) found = true;
            				ArrayList<String> newList = new ArrayList<String>(list);
            				newList.add(s);
            				resultList.add(newList);
            			}
            		}
            		array[j] = base;
            	}
            }
            
            if(found) {
            	ArrayList<ArrayList<String>> result = new ArrayList<ArrayList<String>>();
            	for(ArrayList<String> list : resultList) {
            		if(list.get(list.size() - 1).equals(end)) result.add(list);
            	}
            	return result;
            }
          
        }
        return new ArrayList<ArrayList<String>>();
    }
}