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
        ArrayList<ArrayList<String>> result = new ArrayList<ArrayList<String>>();
        int currentLevel = 1;
        int nextLevel = 0;
        boolean found = false;
        HashSet<String> visited = new HashSet<String>();
        
        Queue<String> q = new LinkedList<String>();
        q.add(start);
        Queue<ArrayList<String>> sequences = new LinkedList<ArrayList<String>>();
        ArrayList<String> l = new ArrayList<String>();
        l.add(start);
        sequences.add(l);
        
        while(!q.isEmpty()) {
            String st = q.remove();
            ArrayList<String> temp = sequences.remove();
            currentLevel--;
            if(st.equals(end)) {
                result.add(temp);
                found = true;
            } else {
                if(!found) {
                    for(int i = 0; i < st.length(); i++) {
                        StringBuffer sb = new StringBuffer(st);
                        for(int j = 0; j < 26; j++) {
                            sb.setCharAt(i, (char)('a' + j));
                            String next = sb.toString();
                            boolean in = false;
                            for(int g = 0; j < temp.size(); g++) {
                                if(temp.get(g).equals(next)) {
                                    in = true;
                                    break;
                                }
                            }
                            if(dict.contains(next) && !in) {
                                q.add(next);
                                visited.add(next);
                                nextLevel++;
                                ArrayList<String> nexttemp = new ArrayList<String>(temp);
                                nexttemp.add(next);
                                sequences.add(nexttemp);
                            }
                        }
                    }
                }
            }
            if(currentLevel == 0) {
                if(found) {
                    break;
                } else {
                    currentLevel = nextLevel;
                    nextLevel = 0;
                }
            }
        }
        return result;
    }
}