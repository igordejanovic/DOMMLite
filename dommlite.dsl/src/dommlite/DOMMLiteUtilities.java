/*
 *
 * $Id$
*/
package dommlite;

public class DOMMLiteUtilities {
	public static String packageNameToPath(String packageName){
		return packageName.replace('.', '/');
	}
	public static String dateAndTime(){
		return new java.util.Date().toString();
	}
	public static String escape(String str_to_escape){
		return str_to_escape.replace("\'", "\\\'");
	}

}