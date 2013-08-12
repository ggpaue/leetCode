
public class Solution {
	public boolean isPalindrome(String s) {
		int left = 0;
		int right = s.length() - 1;
		while(right >= left) {
			char leftChar, rightChar;
			int tempLeft = left, tempRight = right;
			do {
				leftChar = Character.toLowerCase(s.charAt(tempLeft));
				tempLeft++;
			} while(!isLetterOrDigit(leftChar) && tempLeft <= right);
			do {
				rightChar = Character.toLowerCase(s.charAt(tempRight));
				tempRight--;	
			} while(!isLetterOrDigit(rightChar) && left <= tempRight);
			
			if(leftChar != rightChar && (tempRight+1) >= (tempLeft-1)) return false;
			
			left = tempLeft;
			right = tempRight;
		}
		return true;
	}
	public boolean isLetterOrDigit(char c) {
		return Character.isLetter(c) || Character.isDigit(c);
	}

}
