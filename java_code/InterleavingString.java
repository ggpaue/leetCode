
public class Solution {
	public boolean isInterleave(String s1, String s2, String s3) {
		return search(s1, s2, s3, 0, 0, 0);
	}
	
	private boolean search(String s1, String s2, String s3, int i1, int i2, int i3) {
		int len1 = s1.length(), len2 = s2.length();
		if(i1 < len1 && i2 < len2) {
			boolean result = false;
			if(s1.charAt(i1) == s3.charAt(i3)) {
				i1++;
				i3++;
				result = search(s1, s2, s3, i1, i2, i3);
				if(result) {
					return true;
				} else {
					i1--;
					i3--;
				}
			}
			
			if(s2.charAt(i2) == s3.charAt(i3)) {
				i2++;
				i3++;
				result = search(s1, s2, s3, i1, i2, i3);
				return result;
			}
			return false;
		}
		if(i1 < len1) {
			return s1.substring(i1).compareTo(s3.substring(i3)) == 0;
		}
		
		return s2.substring(i2).compareTo(s3.substring(i3)) == 0;
	}

}
