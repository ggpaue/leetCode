/**
 * 
 * Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
 *
 * For example, given n = 3, a solution set is:
 *
 * "((()))", "(()())", "(())()", "()(())", "()()()"
 *  
 */

import java.util.*;
public class Solution {
	public ArrayList<String> generateParenthesis(int n) {
		ArrayList<String> result = new ArrayList<String>();
		if(n == 0) return result;
		int size = n << 1;
		
		Queue<ArrayList<Integer>> queue = new LinkedList<ArrayList<Integer>>();
		ArrayList<Integer> init = new ArrayList<Integer>();
		queue.add(init);
		
		while(queue.isEmpty() == false) {
			ArrayList<Integer> top = queue.poll();
			if(top.size() == size) {
				store(top, result);
			} else {
				int sum = sum(top);
				if(sum == 0) {
					top.add(1);
					queue.add(top);
				} else if(sum == n) {
					top.add(-1);
					queue.add(top);
				} else {
					ArrayList<Integer> temp = (ArrayList<Integer>)top.clone();
					temp.add(-1);
					top.add(1);
					queue.add(temp);
					queue.add(top);
				}
			}
		}
		return result;
	}
	
	public static void store(ArrayList<Integer> list, ArrayList<String> result) {
		int sum = sum(list);
		if(sum != 0) {
			return;
		} else {
			StringBuilder str = new StringBuilder();
			for(int num : list) {
				if(num == -1) {
					str.append(")");
				} else {
					str.append("(");
				}
			}
			
			result.add(str.toString());
		}
		
	}
	
	public static int sum(ArrayList<Integer> list) {
		int sum = 0;
		for(int num : list) {
			sum += num;
			
		}
		return sum;
	}

}
