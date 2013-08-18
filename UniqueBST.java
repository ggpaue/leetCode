
public class Solution {
	public int numTrees(int n) {
		if(n == 0) return 1;
		if(n == 1) return 1;
		if(n == 2) return 2;
		int sum = 0;
		for(int i=0; i <= n-1; i++) {
			sum += numTrees(i) * numTrees(n-i-1); 
		}
		return sum;
	}

}
