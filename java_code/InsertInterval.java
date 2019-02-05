/**
 * 
 * Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
 * 
 * You may assume that the intervals were initially sorted according to their start times.
 * 
 * Example 1:
 * Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].
 * 
 * Example 2:
 * Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].
 * 
 * This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
 * 
 */
import java.util.ArrayList;
public class Solution {
	public ArrayList<Interval> insert(ArrayList<Interval> intervals, Interval newInterval) {
		if(intervals.size() == 0) intervals.add(newInterval);
		int startPos = searchPosition(intervals, newInterval.start);
		int endPos = searchPosition(intervals, newInterval.end);
		
		int newStart = 0;
		if(startPos >= 0 && intervals.get(startPos).end >= newInterval.start) {
			newStart = intervals.get(startPos).start;
		} else {
			newStart = newInterval.start;
			startPos++;
		}
		
		int newEnd = 0;
		if(endPos >= 0) {
			newEnd = Math.max(newInterval.end, intervals.get(endPos).end);
		} else {
			newEnd = newInterval.end;
		}
		
		for(int i = startPos; i < endPos + 1; i++) {
			intervals.remove(startPos);
		}
		intervals.add(startPos, new Interval(newStart, newEnd));
		return intervals;
	}
	
	public int searchPosition(ArrayList<Interval> intervals, int x) {
		int a = 0;
		int b = intervals.size() - 1;
		
		while(a <= b) {
			int mid = (a + b) / 2;
			if(intervals.get(mid).start == x) {
				return mid;
			} else if(intervals.get(mid).start > x) {
				b = mid - 1;
			} else {
				a = mid + 1;
			}
		}
		return b;
	}
	
	public static void main(String[] args) {
		ArrayList<Integer> result = new ArrayList<Integer>();
		result.add(1);
		result.add(2);
		result.add(3);
		result.add(1, 4);
		System.out.print(result);
	}

}
