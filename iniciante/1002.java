import java.io.IOException;
import java.util.*;

public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner teclado = new Scanner(System.in);
		double raio = teclado.nextDouble();
		
		raio = 3.14159 * raio * raio;
		
		String r = String.format("%.4f", raio);
		
		System.out.println("A="+ r);
    }
 
}