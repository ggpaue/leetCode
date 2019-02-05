/**
 * 
 * Given a collection of intervals, merge all overlapping intervals.
 * For example,
 * Given [1,3],[2,6],[8,10],[15,18],
 * return [1,6],[8,10],[15,18]. 
 *  
 */


import java.util.*;
public class Solution {
	public ArrayList<Interval> merge(ArrayList<Interval> intervals) {
		int size= intervals.size();
		int count;
		do {
			count = 0;
			for(int i = 0; i < size; i++) {
				Interval interval1 = intervals.get(i);
				if(interval1 != null) {
					for(int j = 0; j < size; j++) {
						Interval interval2 = intervals.get(j);
						if(i != j && interval2 != null && check(interval1, interval2)) {
							interval1 = merge(interval1, interval2);
							intervals.set(i, interval1);
							intervals.set(j, null);
							count++;
						}
					}
				}
			}
		} while(count != 0);
		ArrayList<Interval> result = new ArrayList<Interval>();
		for(Interval item : intervals) {
			if(item != null) {
				result.add(item);
			}
		}
		return result;
	}
	
	private Interval merge(Interval interval1, Interval interval2) {
		return new Interval(Math.min(interval1.start, interval2.start), Math.max(interval1.end, interval2.end));
	}
	
	private boolean check(Interval interval1, Interval interval2) {
		return !(interval1.end < interval2.start || interval1.start > interval2.end);
	}

}
