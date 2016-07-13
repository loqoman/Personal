import edu.uweo.javaintro.tools.Turtle;
public class First_Turtle{
	public static void main( String[] args){
		Turtle dorothy = new Turtle(); 
		dorothy.paint(45,128);   
		dorothy.paint(-45,256);
		dorothy.paint(-135,256);
		dorothy.move( -45, 128);
		dorothy.swingAround( 15 );
	
		Turtle spot = new Turtle();
		spot.move( 90, 256);
		spot.swingAround( 64 );
	
	
	}
	
}